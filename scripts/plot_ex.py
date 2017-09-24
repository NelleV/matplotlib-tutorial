# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2*X)

ax = plt.axes([0.025, 0.025, 0.95, 0.95])

ax.plot(X, Y+1, color='blue', alpha=1.00)
ax.fill_between(X, 1, Y+1, color='blue', alpha=.25)

ax.plot (X, Y-1, color='blue', alpha=1.00)
ax.fill_between(X, -1, Y-1, (Y-1) > -1, color='blue', alpha=.25)
ax.fill_between(X, -1, Y-1, (Y-1) < -1, color='red',  alpha=.25)

ax.set_xlim(-np.pi, np.pi), plt.xticks([])
ax.set_ylim(-2.5, 2.5), plt.yticks([])
# savefig('../figures/plot_ex.png',dpi=48)
plt.show()
