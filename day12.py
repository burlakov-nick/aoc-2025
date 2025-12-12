from aoc import *


def solve(r: Reader):
    *_, tests = r.read_blocks(remove=[":", "x"])
    print(sum(1 for n, m, *counts in tests if sum(counts) * 7 <= n * m))


run(solve, skip_sample=True)
