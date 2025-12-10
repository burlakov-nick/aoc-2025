from z3 import *

from aoc import *
from helpers import *


def part_1(target, switches):
    switches = [sum((1 << i) for i in s) for s in switches]

    q, cur = [0], 0
    d = defaultdict(lambda: 1_000_000_000)
    d[0] = 0
    while cur < len(q) and q[cur] != target:
        x = q[cur]
        for s in switches:
            y = x ^ s
            if d[y] > d[x] + 1:
                d[y] = d[x] + 1
                q.append(y)
        cur += 1
    return d[target]


def part_2(target, switches):
    def find_min_coefficients(vectors, target):
        n = len(vectors)
        dim = len(target)

        # Create integer variables for coefficients
        y = [Int(f"y_{i}") for i in range(n)]

        opt = Optimize()

        # Constraint: y[0]*x[0] + y[1]*x[1] + ... == target
        for d in range(dim):
            opt.add(Sum([y[i] * vectors[i][d] for i in range(n)]) == target[d])

        # constrain y to be non-negative
        for i in range(n):
            opt.add(y[i] >= 0)

        # Minimize sum of coefficients
        opt.minimize(Sum(y))

        if opt.check() == sat:
            model = opt.model()
            return [model[y[i]].as_long() for i in range(n)]
        return None

    n = len(target)
    vectors = [tuple(1 if i in s else 0 for i in range(n)) for s in switches]
    return sum(find_min_coefficients(vectors, target))


def solve(r: Reader):
    res1, res2 = 0, 0
    for line in r.read_lines():
        lights, *switches, jolts = line.split()
        switches = [parse_values(s[1:-1], ",") for s in switches]

        target = sum((1 << i) for i, c in enumerate(lights[1:-1]) if c == "#")
        res1 += part_1(target, switches)

        target2 = tuple(parse_values(jolts[1:-1], ","))
        res2 += part_2(target2, switches)

    print(res1, res2)


run(solve)
