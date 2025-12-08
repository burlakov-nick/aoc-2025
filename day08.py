from functools import reduce
from itertools import combinations
from operator import mul

from aoc import *
from helpers import *
from vec import *


def solve(r: Reader):
    xs = [V3(x, y, z) for x, y, z in r.read(remove=",")]
    num_pairs = r.extra
    dsu = DSU(xs)
    pairs = sorted(combinations(xs, 2), key=lambda p: p[0].dist_to(p[1]))

    for x, y in pairs[:num_pairs]:
        dsu.merge(x, y)

    print(reduce(mul, sorted([len(c) for c in dsu], reverse=True)[:3]))

    last_connected = None
    for x, y in pairs[num_pairs:]:
        if dsu.merge(x, y):
            last_connected = x, y

    print(last_connected[0].x * last_connected[1].x)


run(solve, sample=10, input=1000)
