from aoc import *
from helpers import *


def can_be_removed(rolls, p):
    return sum(1 for x in p.neighbors_8() if x in rolls) < 4


def removable(rolls):
    return set(p for p in rolls if can_be_removed(rolls, p))


def solve(r: Reader):
    grid, n, m = r.read_grid_dict_v()
    initial_rolls = set(p for p, v in grid.items() if v == "@")
    rolls = set(initial_rolls)
    print(len(removable(rolls)))

    while len(removed := removable(rolls)):
        rolls -= removed
    print(len(initial_rolls) - len(rolls))


run(solve)
