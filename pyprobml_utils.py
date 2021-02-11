import os
import matplotlib.pyplot as plt

figdir = '../figures'


def save_fig(fname, *args, **kwargs) -> None:
    plt.tight_layout()
    plt.savefig(os.path.join(figdir, fname), *args, **kwargs)
