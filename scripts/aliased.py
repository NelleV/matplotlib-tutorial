import matplotlib.pyplot as plt

size = 128,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
ax = fig.add_axes([0,0,1,1], frameon=False)

plt.rcParams['text.antialiased'] = False
ax.text(0.5,0.5,"Aliased",ha='center',va='center')

plt.xlim(0,1),plt.ylim(0,1),
plt.xticks([]),plt.yticks([])

fig.savefig('../figures/aliased.png', dpi=dpi)
