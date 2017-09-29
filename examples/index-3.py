from gwemlightcurves.KNModels import KNTable
from gwpy.table import EventTable
t = KNTable.read_samples('posterior_samples.dat')
t = t.calc_tidal_lambda(remove_negative_lambda=True)
t = t.calc_compactness(fit=True)
t = t.calc_baryonic_mass(EOS='mpa1', TOV='Monica', fit=True)
t = KNTable.model('Me2017', t)
t = EventTable(t)
plot = t.plot('t', 'lbol')
plot.show()
