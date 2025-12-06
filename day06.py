from functools import reduce
from itertools import pairwise
from operator import add, mul

from aoc import *
from helpers import *


def calc(raw_nums, ops, get_nums):
    s = 0
    for raw, op in zip(raw_nums, ops):
        nums = get_nums(raw)
        s += reduce(add if op == "+" else mul, nums)
    return s


def get_nums_1(raw):
    return [int(x) for x in raw]


def get_nums_2(raw):
    return [int("".join(x)) for x in transpose(raw)]


def solve(r: Reader):
    *lines, ops = r.read_lines()
    ops = parse_values(ops)

    spaces = [
        -1,
        *(i for i in range(len(lines[0])) if all(line[i] == " " for line in lines)),
        len(lines[0]),
    ]
    raw_nums = [[line[l + 1 : r] for line in lines] for l, r in pairwise(spaces)]

    print(calc(raw_nums, ops, get_nums_1))
    print(calc(raw_nums, ops, get_nums_2))


run(solve)
