from gwemlightcurves.EjectaFits.DiUj2017 import calc_meje, calc_vej
from gwemlightcurves.KNModels import KNTable
from gwpy.table import EventTable
from gwpy.plotter import EventTablePlot
t = KNTable.read_samples('posterior_samples.dat')
t_indepedent = KNTable.read_samples('posterior_samples.dat')
t = t.calc_tidal_lambda(remove_negative_lambda=True)
t_indepedent = t_indepedent.calc_tidal_lambda(remove_negative_lambda=True)
t = t.downsample(Nsamples=1000)
t_indepedent = t_indepedent.downsample(Nsamples=1000)

plot = EventTablePlot(figsize=(18.5, 10.5))
EOS = ['ap3', 'ap4', 'eng', 'gnh3', 'H4', 'mpa1', 'ms1', 'ms1b', 'sly', 'wff1', 'wff2']
Color = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'chartreuse', 'burlywood', 'lightseagreen', 'mediumaquamarine', 'brown']
locations = [(3,4,1), (3,4,2), (3,4,3), (3,4,4), (3,4,5), (3,4,6), (3,4,7), (3,4,8), (3,4,9), (3,4,10), (3,4,11)]
plot_location = dict(zip(EOS, locations))
EOS_Color = dict(zip(EOS, Color))

t_indepedent = t_indepedent.calc_compactness(fit=True)
t_indepedent = t_indepedent.calc_baryonic_mass(EOS=None, TOV=None, fit=True)
t_indepedent['mej'] = calc_meje(t_indepedent['m1'], t_indepedent['mb1'], t_indepedent['c1'], t_indepedent['m2'], t_indepedent['mb2'], t_indepedent['c2'])

for eos in EOS:
    ax = plot.add_subplot(plot_location[eos][0], plot_location[eos][1], plot_location[eos][2])
    ax.set_title('EOS: {0}'.format(eos), fontsize='small')
    for fit in [True, False]:
        t_radius = t.calc_radius(EOS=eos, TOV='Monica')
        t_radius_compact = t_radius.calc_compactness()
        t_radius_compact_bary = t_radius_compact.calc_baryonic_mass(EOS=eos, TOV='Monica', fit=fit)
        t_radius_compact_bary['mej'] = calc_meje(t_radius_compact_bary['m1'], t_radius_compact_bary['mb1'], t_radius_compact_bary['c1'], t_radius_compact_bary['m2'], t_radius_compact_bary['mb2'], t_radius_compact_bary['c2'])
        t_radius_compact_bary = EventTable(t_radius_compact_bary)
        if fit:
            plot.add_scatter(t_radius_compact_bary['m2'], t_radius_compact_bary['mej'], label='Bary From Fit', alpha=0.5, color=EOS_Color[eos], ax=ax)
        else:
            plot.add_scatter(t_radius_compact_bary['m2'], t_radius_compact_bary['mej'], label='Bary From Table', alpha=0.5, color=EOS_Color[eos], marker='*', ax=ax)
    plot.add_scatter(t_indepedent['m2'], t_indepedent['mej'], label='EOS Independent', alpha=0.2, color='grey', marker='+', ax=ax)
    plot.add_legend(loc="upper left", fancybox=True, fontsize='small')

plot.text(0.5, 0.04, 'Mass of Smaller Object', ha='center', fontsize='x-large')
plot.text(0.04, 0.5, 'Ejecta Mass', va='center', rotation='vertical', fontsize='x-large')
plot.suptitle('Smaller Mass by Ejecta Mass', fontsize='x-large')
plot.show()
