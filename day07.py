from functools import cache

from aoc import *
from helpers import *
from vec import *

DOWN, LEFT, RIGHT = V(1, 0), V(0, -1), V(0, 1)


def solve(r: Reader):
    grid, _, _ = r.read_grid_dict_v()
    start = next(p for p, v in grid.items() if v == "S")

    @cache
    def calc(p):
        if p not in grid:
            return set()
        if grid[p] == ".":
            return calc(p + DOWN)
        return {p} | calc(p + LEFT) | calc(p + RIGHT)

    print(len(calc(start)))

    @cache
    def calc_2(p):
        if p not in grid:
            return 1
        if grid[p] == ".":
            return calc_2(p + DOWN)
        return calc_2(p + LEFT) + calc_2(p + RIGHT)

    print(calc_2(start))


run(solve)
