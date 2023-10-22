using CairoMakie
using Combinatorics
using Distributions
using Random

Random.seed!(42);

p = 0.3;
d_geom = Geometric(p);
rvs_geom = rand(d_geom, 10000);

fig = Figure(resolution = (500, 400))
ax = Axis(fig[1, 1])

hist!(ax, rvs_geom; bins = 30, strokewidth = 1, strokecolor = :black)
limits!(ax, -0.5, 20.5, 0, 3100)
ax.title = "Generated Geometric R.V.s"
fig
