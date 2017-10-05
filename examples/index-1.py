from gwemlightcurves.KNModels import KNTable
from gwpy.table import EventTable
from gwpy.plotter import EventTablePlot
t = KNTable.read_samples('posterior_samples.dat')
t = t.calc_tidal_lambda(remove_negative_lambda=True)

plot = EventTablePlot(figsize=(18.5, 10.5))
ax = plot.gca()
EOS = ['ap3', 'ap4', 'eng', 'gnh3', 'H4', 'mpa1', 'ms1', 'ms1b', 'sly', 'wff1', 'wff2']
Color = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'chartreuse', 'burlywood', 'lightseagreen', 'mediumaquamarine', 'brown']
EOS_Color = dict(zip(EOS, Color))

for eos in EOS:
    t_radius = t.calc_radius(EOS=eos, TOV='Monica')
    t_radius_compact = t_radius.calc_compactness()
    t_radius_compact = EventTable(t_radius_compact)
    ax.hist(t_radius_compact['c1'], log=True, bins=20, alpha=0.5, histtype='stepfilled', label='Compactness From {0} Table'.format(eos), color=EOS_Color[eos])

t_comp_fit = t.calc_compactness(fit=True)
ax.hist(t_comp_fit['c1'], log=True, bins=20, alpha=0.2, histtype='stepfilled', label='Compactness From Fit', color='black')

ax.set_xlabel('Compactness')
ax.set_ylabel('Rate')
ax.set_title('Compactness Values')
plot.add_legend()
ax.autoscale(axis='x', tight=True)
plot.show()
