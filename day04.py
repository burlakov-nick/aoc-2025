from aoc import *
from helpers import *


def can_be_removed(grid, p):
    return grid[p] == "@" and sum(1 for x in p.neighbors_8() if grid.get(x) == "@") < 4


def removable(grid):
    return (p for p in grid.keys() if can_be_removed(grid, p))


def solve(r: Reader):
    grid, n, m = r.read_grid_dict_v()
    print(count(removable(grid)))

    total = 0
    while removed := list(removable(grid)):
        for p in removed:
            grid[p] = "."
        total += len(removed)
    print(total)


run(solve)
