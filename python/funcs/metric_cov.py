"""
Original Author: Xavier Yang
Link: https://github.com/ivaquero
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse


def covariance_ellipse(cov, deviations=1):
    U, s, _ = np.linalg.svd(cov)
    orientation = np.arctan2(U[1, 0], U[0, 0])
    width_radius = deviations * np.sqrt(s[0])
    height_radius = deviations * np.sqrt(s[1])

    if height_radius > width_radius:
        raise ValueError("width_radius must be greater than height_radius")

    return (orientation, width_radius, height_radius)


def plot_cov_ellipse(
    ax,
    mean,
    cov,
    stds=[1],
    show_semiaxis=False,
    show_center=True,
    angle=1,
    edgecolor="darkslateblue",
    facecolor="green",
    alpha=0.2,
    label="",
    **line_kwargs,
):
    ellipse = covariance_ellipse(cov)

    angle = np.degrees(ellipse[0])
    width = ellipse[1] * 2.0
    height = ellipse[2] * 2.0

    for sd in stds:
        e = Ellipse(mean, sd * width, sd * height, angle=angle)
        ax.add_patch(e)
        e.set(
            facecolor=facecolor,
            edgecolor=edgecolor,
            alpha=alpha,
            label=label,
            **line_kwargs,
        )

    x, y = mean
    if show_center:
        ax.scatter(x, y, marker="+", color=edgecolor)
    if show_semiaxis:
        a = ellipse[0]
        h, w = height / 4, width / 4
        ax.plot([x, x + h * np.cos(a + np.pi / 2)], [y, y + h * np.sin(a + np.pi / 2)])
        ax.plot([x, x + w * np.cos(a)], [y, y + w * np.sin(a)])

    ax.set(title=f"[{cov[0]}\n   {cov[1]}]")


_, ax = plt.subplots()
mean = [2, 7]
P = [[2, 0], [0, 2]]
std = [1, 2, 3]
plot_cov_ellipse(ax, mean, P, stds=std)
plt.show()
