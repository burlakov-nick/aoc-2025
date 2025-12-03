from aoc import *


def max_jolts(bank, left):
    if not bank or not left:
        return ""
    mx = max(bank[: len(bank) - left + 1])
    pos = bank.find(mx)
    return mx + max_jolts(bank[pos + 1 :], left - 1)


def solve(r: Reader):
    banks = r.read_lines()
    print(sum(int(max_jolts(bank, 2)) for bank in banks))
    print(sum(int(max_jolts(bank, 12)) for bank in banks))


run(solve)
