"""
Original Author: Xavier Yang
Link: https://github.com/ivaquero
"""
from collections import namedtuple
from os import path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

gaussian = namedtuple("Gaussian", ["mean", "var"])
gaussian.__repr__ = lambda s: f"N(μ={s[0]:.3f}, σ²={s[1]**2:.3f})"


def gaussian_product(g1, g2):
    mean = (g1.var * g2.mean + g2.var * g1.mean) / (g1.var + g2.var)
    variance = (g1.var * g2.var) / (g1.var + g2.var)
    return gaussian(mean, variance)


def plot_gaussian_product(ax, xs, g1, g2):
    g_product = gaussian_product(g1, g2)

    for g, ls in zip([g1, g2, g_product], ["-", "-", "--"]):
        ys = [stats.norm(g.mean, g.var**0.5).pdf(x) for x in xs]
        ax.plot(xs, ys, linestyle=ls, label=f"$N({g.mean:.2f}, {g.var:.2f})$")

    ax.grid(1)
    ax.legend()


_, ax = plt.subplots()
g1 = gaussian(1, 10)
g2 = gaussian(5, 5)
xs = np.linspace(-15, 15, 100)
plot_gaussian_product(ax, xs, g1, g2)

filename, extension = path.splitext(path.basename(__file__))
plt.savefig(f"../../images/trials/{filename}.png")
plt.show()
