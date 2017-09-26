from pylab import *
import matplotlib.pyplot as plt

size = 256,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
ax = fig.add_axes([0,0.1,1,.8], frameon=False)

for i in range(1,11):
    ax.axvline(i, linewidth=1, color='blue',alpha=.25+.75*i/10.)

ax.set_xlim(0,11)
ax.set_xticks([]),yticks([])
savefig('../figures/alpha.png', dpi=dpi)
