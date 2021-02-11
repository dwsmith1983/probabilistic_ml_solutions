# Plot pdf and cdf of standard normal

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

from pyprobml_utils import save_fig

X = np.linspace(-3, 3, 500)
rv = norm(0, 1)
fig, ax = plt.subplots()
ax.plot(X, rv.pdf(X))
plt.title("Gaussian pdf")
save_fig("gaussian1d.pdf")
plt.show()

fig, ax = plt.subplots()
ax.plot(X, rv.cdf(X))
plt.title("Gaussian cdf")
save_fig("gaussianCdf.pdf")
plt.show()
