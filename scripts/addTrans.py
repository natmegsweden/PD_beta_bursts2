# -*- coding: utf-8 -*-
"""
Get transformation MRI <-> MEG with MNE coregistration. Tthis script is run
manually for each subject.

Vinding, M. C., Eriksson, A., Low, C. M. T., Waldthaler, J., Ferreira, D., Ingvar, M., Svenningsson, P., & Lundqvist, D. (2021). Different features of the cortical sensorimotor rhythms are uniquely linked to the severity of specific symptoms in Parkinson's disease. medRxiv.org. https://doi.org/10.1101/2021.06.27.21259592

@author: mcvinding
"""
import mne
import sys
import os.path as op
sys.path.append('/home/mikkel/PD_longrest/scripts/')
from PDbb2_SETUP import meg_path, fs_subjects_dir

#%% Coregistration
# Make sure to give consistent naming when saving -trans files, e.g. "0523-trans.fif"

# Specify subject id
subj = '0525'

#%% Do coregistration
print('------------------ Sub: '+subj+' ------------------')
if sys.platform == 'linux':
    inst = op.join(meg_path, subj, subj+'-ica-raw2.fif')
else:
    inst = 'X:/PD_longrest/meg_data/'+subj+'/'+subj+'-ica-raw.fif'
    
mne.gui.coregistration(subject=subj, subjects_dir=fs_subjects_dir, head_high_res=True, inst=inst)

#%% Inspect
# The transformation file obtained by coregistration
#trans = op.join(meg_path, subj, 'trans.fif')
#
#info = mne.io.read_info(raw_fname)
## Here we look at the dense head, which isn't used for BEM computations but
## is useful for coregistration.
#mne.viz.plot_alignment(info, trans, subject=subject, dig=True,
#                       meg=['helmet', 'sensors'], subjects_dir=subjects_dir,
#                       surfaces='head-dense')

#END
