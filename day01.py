import aoc
import helpers as h
import vec


def count_zeros(s, xs):
    return h.count(((s := (s + x + 100) % 100) for x in xs), 0)


def solve(r: aoc.Reader):
    s = r.read_lines()
    d = [-int(x[1:]) if x[0] == "L" else int(x[1:]) for x in s]
    print(count_zeros(50, d))
    d = h.flatten([[vec.sign(x)] * abs(x) for x in d])
    print(count_zeros(50, d))


aoc.run(solve)
