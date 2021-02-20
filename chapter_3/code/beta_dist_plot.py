import numpy as np
import matplotlib.pyplot as plt
from pyprobml_utils import save_fig
from scipy.stats import beta


x = np.linspace(0, 1, 100)
aa = [0.1, 1., 2, 2., 8.]
bb = [0.1, 1., 2, 3., 4.]
props = ['b-', 'r:', 'k-.', 'g--', 'c-']
for a, b, p in zip(aa, bb, props):
    y = beta.pdf(x, a, b)
    plt.plot(y, p, lw=3, label='a=%.1f,b=%.1f' % (a, b))
plt.legend(loc='upper left')
save_fig('betadist.pdf')
plt.show()
