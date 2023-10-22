import matplotlib.pyplot as plt
from metric_cov import plot_cov_ellipse
from metric_utils import multi_guassian_product

P0 = [[6, 0], [0, 6]]
P1 = [[2, 1.9], [1.9, 2]]
P2 = multi_guassian_product((10, 10), P0, (10, 10), P1)[1]

_, ax = plt.subplots(figsize=(6, 4))

plot_cov_ellipse(
    ax, (10, 10), P0, edgecolor="k", facecolor="yellow", alpha=0.2, label="prior"
)
plot_cov_ellipse(
    ax, (10, 10), P1, edgecolor="k", facecolor="green", alpha=0.5, label="likelihood"
)
plot_cov_ellipse(
    ax, (10, 10), P2, edgecolor="k", facecolor="navy", alpha=0.8, label="posterior"
)
ax.legend()
plt.show()