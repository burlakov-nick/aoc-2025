from itertools import combinations

import matplotlib.pyplot as plt

from aoc import *
from vec import *


def plot2d(xs: list[V], red: V | None = None):
    xs = [(v.x, v.y) for v in xs]
    x, y = zip(*xs, xs[0])
    plt.plot(x, y)
    if red is not None:
        plt.plot(red.x, red.y, "ro", markersize=10)
    plt.show()


def solve(r: Reader):
    ps = [V(x, y) for x, y in r.read(remove=",")]
    print(max(Rec(p1, p2).grid_area() for p1, p2 in combinations(ps, 2)))

    # to see pacman
    # plot2d(xs)
    # s = sorted(((p1, p2) for p1, p2 in pairwise(xs)), key=lambda p: p[0].mdist_to(p[1]), reverse=True)
    # print(s[:2])

    upper = V(94860, 50423)
    lower = V(94860, 48342)

    upper_ps = [p for p in ps if p.y > upper.y]
    lower_ps = [p for p in ps if p.y < lower.y]

    def anyone_inside(rec: Rec, ps):
        return any(p for p in ps if rec.strict_inside(p))

    best_upper = max(
        (Rec(p, upper).grid_area(), p)
        for p in upper_ps
        if not anyone_inside(Rec(p, upper), upper_ps)
    )
    best_lower = max(
        (Rec(p, lower).grid_area(), p)
        for p in lower_ps
        if not anyone_inside(Rec(p, lower), lower_ps)
    )
    best = max(best_upper, best_lower)

    print(best)
    # see the answer
    plot2d(ps, best[1])


run(solve, skip_sample=True)
