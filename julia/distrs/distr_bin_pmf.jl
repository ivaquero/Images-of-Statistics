using CairoMakie
using Combinatorics
using Distributions
using Random

Random.seed!(42);

n = 20 * 12 * 5;
p = 1 / 1000;
λ = p * n;

d_poisson = Poisson(λ);
rvs_poisson = rand(d_poisson, 1000);

fig = Figure(resolution = (500, 400));
ax = Axis(fig[1, 1]);

hist!(ax, rvs_poisson; bins = 10, strokewidth = 1, strokecolor = :black);
limits!(ax, -0.5, 6.5, 0, 400);
ax.title = "Generated Poisson R.V.s"
fig
