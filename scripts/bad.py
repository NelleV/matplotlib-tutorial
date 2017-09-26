import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,4),dpi=72)
axes = fig.add_axes([0.01, 0.01, .98, 0.98])
X = np.linspace(0,2,200,endpoint=True)
Y = np.sin(2*np.pi*X)
ax.plot (X, Y, lw=.25, c='k')
ax.set_xticks(np.arange(0.0, 2.0, 0.1))
ax.set_yticks(np.arange(-1.0,1.0, 0.1))
plt.grid()
fig.savefig('../figures/bad.png', dpi=72)
