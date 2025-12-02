from aoc import *
from helpers import *


def is_invalid(p):
    p = str(p)
    return p[: len(p) // 2] == p[len(p) // 2 :]


def is_invalid_2(p):
    p = str(p)
    return any(len(set(batch(p, k))) == 1 for k in range(1, len(p) // 2 + 1))


def solve(r: Reader):
    ranges = list(batch(r.read(remove=[",", "-"])[0], 2))
    print(sum(i for l, r in ranges for i in range(l, r + 1) if is_invalid(i)))
    print(sum(i for l, r in ranges for i in range(l, r + 1) if is_invalid_2(i)))


run(solve)
