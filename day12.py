from aoc import *
from helpers import *


def solve(r: Reader):
    *shapes, tests = r.read_blocks(remove=[":", "x"])
    shapes = [flatten(shape)[1:] for shape in shapes]
    shape_areas = [count(flatten(shape), "#") for shape in shapes]

    def is_ok(test):
        n, m, *counts = test
        return sum(c * a for c, a in zip(counts, shape_areas)) <= n * m

    print(count(tests, is_ok))


run(solve, skip_sample=True)
