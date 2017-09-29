from gwemlightcurves.KNModels import KNTable
from gwpy.table import EventTable
t = KNTable.read_samples('posterior_samples.dat')
t = t.calc_tidal_lambda(remove_negative_lambda=True)
t_sly_mon = t.calc_radius(EOS='sly', TOV='Monica'); t_H4_mon = t.calc_radius(EOS='H4', TOV='Monica'); t_mpa1_mon = t.calc_radius(EOS='mpa1', TOV='Monica'); t_ms1_mon = t.calc_radius(EOS='ms1', TOV='Monica'); t_ms1b_mon = t.calc_radius(EOS='ms1b', TOV='Monica');
t_sly_mon = t_sly_mon.calc_compactness(); t_H4_mon = t_H4_mon.calc_compactness(); t_mpa1_mon = t_mpa1_mon.calc_compactness(); t_ms1_mon = t_ms1_mon.calc_compactness(); t_ms1b_mon = t_ms1b_mon.calc_compactness()
t_comp_fit = t.calc_compactness(fit=True)
t_sly_mon = EventTable(t_sly_mon); t_H4_mon = EventTable(t_H4_mon); t_mpa1_mon = EventTable(t_mpa1_mon); t_ms1_mon = EventTable(t_ms1_mon); t_ms1b_mon = EventTable(t_ms1b_mon); t_comp_fit = EventTable(t_comp_fit);
plot = t_sly_mon.hist('c1', bins=20, histtype='stepfilled', label='Compactness Monica Sly')
ax = plot.gca()
ax.hist(t_H4_mon['c1'], logbins=True, bins=20, histtype='stepfilled', label='Compactness Monica H4'); ax.hist(t_mpa1_mon['c1'], logbins=True, bins=20, histtype='stepfilled', label='Compactness Monica mpa1'); ax.hist(t_ms1_mon['c1'], logbins=True, bins=20, histtype='stepfilled', label='Compactness Monica ms1'); ax.hist(t_ms1b_mon['c1'], logbins=True, bins=20, histtype='stepfilled', label='Compactness Monica ms1b'); ax.hist(t_comp_fit['c1'], logbins=True, bins=20, histtype='stepfilled', label='Compactness From Fit')
ax.set_xlabel('Compactness')
ax.set_ylabel('Rate')
ax.set_title('Compactness Values')
plot.add_legend()
ax.autoscale(axis='x', tight=True)
