
# Plot regression models with clinical scores


library(ggplot2)

# Load models
setwd("/Users/huser/Documents/analysis")
load(file="updrsmods.RData")


a.labels <- c("Rate", "Length", "Interval", "Amplitude",
              "1/f offset", "1/f exponent", "Alpha power", "Alpha centre freq.", "Beta power", "Beta centre freq.",
              "Age", "Sex", "Cortical thickness", "Levodopa equivalent daily dosage", "Disease duration")
a.labels <- rev(a.labels)
m.labels <- c("total MDS-UPDRS III", 
              "Midline function", 
              "Rest tremor", 
              "Rigidity", 
              "Bradykinesia right upper limb", 
              "Bradykinesia left upper limb", 
              "Postural and kinetic tremor", 
              "Bradykinesia lower limb")
m.labels <- rev(m.labels)

updrs.plt <- plot_models(mods, grid = TRUE, std.est = NULL, transform = NULL, axis.lim=c(-2,2),
                         axis.labels = a.labels, m.labels = m.labels, vline.color = "gray",
                         show.values = TRUE, show.p = FALSE, p.shape = FALSE, auto.label = FALSE, show.legend = FALSE,
                         digits = 3, value.size=3, colors="bw")
updrs.plt <- updrs.plt + scale_y_continuous(limits=c(-2.5, 2)) + theme_bw()
updrs.plt

ggsave("modplt_updrs.png", updrs.plt, dpi=900,
       width=140, height=50, units="mm", scale=3)

#END


# Load models
load(file="updrsmods.RData")

mods <- list(Fmod.x, F1mod.x, F2mod.x, F3mod.x, F4mod.x, F5mod.x, F6mod.x, F7mod.x)
mods <- rev(mods)

a.labels <- c("Rate", "Length", "Interval", "Amplitude",
              "1/f offset", "1/f exponent", "Alpha power", "Alpha centre freq.", "Beta power", "Beta centre freq.",
              "Age", "Sex", "Cortical thickness", "Levodopa equivalent daily dosage", "Disease duration")
a.labels <- rev(a.labels)
m.labels <- c("total MDS-UPDRS III", 
              "Midline function", 
              "Rest tremor", 
              "Rigidity", 
              "Bradykinesia right upper limb", 
              "Bradykinesia left upper limb", 
              "Postural and kinetic tremor", 
              "Bradykinesia lower limb")
m.labels <- rev(m.labels)

updrs.plt <- plot_models(mods, grid = TRUE, std.est = NULL, transform = NULL, axis.lim=c(-2,2),
                         axis.labels = a.labels, m.labels = m.labels, vline.color = "gray",
                         show.values = TRUE, show.p = FALSE, p.shape = FALSE, auto.label = FALSE, show.legend = FALSE,
                         digits = 3, value.size=3, colors="bw")
updrs.plt <- updrs.plt + scale_y_continuous(limits=c(-2.5, 2)) + theme_bw()

ggsave("modplt_updrs.png", updrs.plt, dpi=900,
       width=140, height=50, units="mm", scale=3)

#END
