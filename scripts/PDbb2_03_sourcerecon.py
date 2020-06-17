#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Do MNE on resting state data. 
@author: mikkel
"""
import os.path as op
from mne import read_forward_solution, read_cov
# from mne import make_bem_model, make_bem_solution, make_forward_solution
# from mne import write_bem_solution, write_forward_solution
from mne.io import Raw
from mne.minimum_norm import make_inverse_operator, apply_inverse_raw
import time
import sys
sys.path.append('/home/mikkel/PD_longrest/scripts')
from PDbb2_SETUP import subjects, meg_path, spacing

#%% Run settings
overwrite = False

#%% Initiate values
conductivity = (0.3,)                               # for single layer
#lambda2 = 0.0000001

snr = 2.0                           # Standard assumption for average data is 3.0
lambda2 = 1.0 / snr ** 2

no_raw = []
no_cov = []
no_fwd = []

#%% SUBJECT LOOP HERE ####
for ii, subj in enumerate(subjects):
    print('NOW PROCESSING: '+subj)
    subj_path   = op.join(meg_path, subj)
    rawfile     = op.join(subj_path, subj+'-ica-raw.fif')
    covfile     = op.join(subj_path, subj+'-cov.fif') 
    fwdfile     = op.join(subj_path, subj+'-'+spacing+'-fwd.fif')
    outfname    = op.join(subj_path, subj+'-dspm')      #NB omit file ending!
    
    if op.exists(outfname+'-lh.stc') and not overwrite:
        print('Output '+outfname+' already exists. Will not overwrite!')
        continue
                     
    # Read raw data
    if op.isfile(rawfile):
        raw = Raw(rawfile, preload=False)
    else:
        no_raw += [subj]
        continue
            
    # Read forward model
    if op.isfile(fwdfile):
        fwd = read_forward_solution(fwdfile)
    else:
        no_fwd += [subj]
        continue
        
    if op.isfile(covfile):
        cov = read_cov(covfile)
    else:
        no_cov += [subj]
        continue

    # Make (or read) inverse operator
    inv = make_inverse_operator(raw.info, fwd, cov)
            
    # Do source recon
    t0 = time.time()
    stc_dSPM = apply_inverse_raw(raw, inv, lambda2, method="dSPM")
    dt = time.time() - t0
    print('Time elapsed: '+str(dt/60.0)+' min')
        
    # Save
    stc_dSPM.save(outfname)

#END