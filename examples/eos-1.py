from distutils.spawn import find_executable
from gwemlightcurves.KNModels import table
from gwpy.table import EventTable
from gwpy.plotter import EventTablePlot

plot = EventTablePlot(figsize=(18.5, 10.5))
ax = plot.gca()
EOS = ['ap3', 'ap4', 'eng', 'gnh3', 'H4', 'mpa1', 'ms1', 'ms1b', 'sly', 'wff1', 'wff2']
Color = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'chartreuse', 'burlywood', 'lightseagreen', 'mediumaquamarine', 'brown']
EOS_Color = dict(zip(EOS, Color))

for eos in EOS:
    t=EventTable.read(find_executable(eos+'_mr.dat'), format='ascii')
    mask=t['radius']<20
    ax.plot(t['radius'][mask], t['mass'][mask], color=EOS_Color[eos], label=eos)
ax.set_xlabel("Radius (km)")
ax.set_ylabel("Mass ($M_{\odot}$)")
ax.set_title('Monica Mass Radius Curves')
plot.add_legend()
