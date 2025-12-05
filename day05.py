from aoc import *
from helpers import *


def merge_ranges(ranges):
    ranges.sort()

    merged = [ranges[0]]
    for l, r in ranges[1:]:
        last_l, last_r = merged[-1]
        if l <= last_r + 1:
            merged[-1] = (last_l, max(last_r, r))
        else:
            merged.append((l, r))
    return merged


def solve(reader: Reader):
    ranges, ingredients = reader.read_blocks(remove="-")
    ingredients = flatten(ingredients)

    def is_fresh(x):
        return any(1 for l, r in ranges if l <= x <= r)

    print(count(ingredients, is_fresh))

    ranges = merge_ranges(ranges)
    print(sum(r - l + 1 for l, r in ranges))


run(solve)
