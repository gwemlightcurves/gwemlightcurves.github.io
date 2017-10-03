from gwemlightcurves.KNModels import KNTable
from gwpy.table import EventTable
t = KNTable.read_samples('posterior_samples.dat')
t = t.calc_tidal_lambda(remove_negative_lambda=True)
t_sly_mon = t.calc_radius(EOS='sly', TOV='Monica'); t_H4_mon = t.calc_radius(EOS='H4', TOV='Monica'); t_mpa1_mon = t.calc_radius(EOS='mpa1', TOV='Monica'); t_ms1_mon = t.calc_radius(EOS='ms1', TOV='Monica'); t_ms1b_mon = t.calc_radius(EOS='ms1b', TOV='Monica');
t_sly_mon = t_sly_mon.calc_compactness(); t_H4_mon = t_H4_mon.calc_compactness(); t_mpa1_mon = t_mpa1_mon.calc_compactness(); t_ms1_mon = t_ms1_mon.calc_compactness(); t_ms1b_mon = t_ms1b_mon.calc_compactness()
t_sly_mon = t_sly_mon.calc_baryonic_mass(EOS='sly', TOV='Monica'); t_H4_mon = t_H4_mon.calc_baryonic_mass(EOS='H4', TOV='Monica'); t_mpa1_mon = t_mpa1_mon.calc_baryonic_mass(EOS='mpa1', TOV='Monica'); t_ms1_mon = t_ms1_mon.calc_baryonic_mass(EOS='ms1', TOV='Monica'); t_ms1b_mon = t_ms1b_mon.calc_baryonic_mass(EOS='ms1b', TOV='Monica')
t_sly_mon_bary_fit = t_sly_mon.calc_baryonic_mass(EOS=None, TOV=None, fit=True); t_H4_mon_bary_fit = t_H4_mon.calc_baryonic_mass(EOS=None, TOV=None, fit=True); t_mpa1_mon_bary_fit = t_mpa1_mon.calc_baryonic_mass(EOS=None, TOV=None, fit=True); t_ms1_mon_bary_fit = t_ms1_mon.calc_baryonic_mass(EOS=None, TOV=None, fit=True); t_ms1b_mon_bary_fit = t_ms1b_mon.calc_baryonic_mass(EOS=None, TOV=None, fit=True)
t_sly_mon = EventTable(t_sly_mon); t_H4_mon = EventTable(t_H4_mon); t_mpa1_mon = EventTable(t_mpa1_mon); t_ms1_mon = EventTable(t_ms1_mon); t_ms1b_mon = EventTable(t_ms1b_mon); t_sly_mon_bary_fit = EventTable(t_sly_mon_bary_fit); t_H4_mon_bary_fit = EventTable(t_H4_mon_bary_fit); t_mpa1_mon_bary_fit = EventTable(t_mpa1_mon_bary_fit); t_ms1_mon_bary_fit = EventTable(t_ms1_mon_bary_fit); t_ms1b_mon_bary_fit = EventTable(t_ms1b_mon_bary_fit)
plot = t_sly_mon.plot('m1','mb1', label='M1 MB1 Monica Sly Bary From Table')
ax = plot.gca()
ax.scatter(t_sly_mon_bary_fit['m1'], t_sly_mon_bary_fit['mb1'], label='M1 MB1 Monica Sly Bary From Fit'); ax.scatter(t_H4_mon['m1'], t_H4_mon['mb1'], label='M1 MB1 Monica H4 Bary From Table'); ax.scatter(t_H4_mon_bary_fit['m1'], t_H4_mon_bary_fit['mb1'], label='M1 MB1 Monica H4 Bary From Fit'); ax.scatter(t_ms1_mon['m1'], t_ms1_mon['mb1'], label='M1 MB1 Monica ms1 Bary From Table'); ax.scatter(t_ms1_mon_bary_fit['m1'], t_ms1_mon_bary_fit['mb1'], label='M1 MB1 Monica ms1 Bary From Fit')
ax.set_xlabel('M1')
ax.set_ylabel('MB1')
ax.set_title('M1 by MB1')
plot.add_legend()
ax.autoscale(axis='x', tight=True)
