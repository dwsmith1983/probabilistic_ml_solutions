import os
import matplotlib.pyplot as plt

figdir = '../figures'


def save_fig(fname): plt.savefig(os.path.join(figdir, fname))
