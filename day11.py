from functools import cache

from aoc import *


def solve(r: Reader):
    g = {x: y for x, *y in r.read(remove=":")}

    @cache
    def rec(x):
        if x == "out":
            return 1
        return sum(rec(y) for y in g[x])

    print(rec("you"))

    @cache
    def rec2(x, dac=False, fft=False):
        if x == "out":
            return int(dac and fft)
        dac |= x == "dac"
        fft |= x == "fft"
        return sum(rec2(y, dac, fft) for y in g[x])

    print(rec2("svr"))


run(solve, skip_sample=True)
