from collections import defaultdict, deque
from collections.abc import Callable, Iterable
from itertools import islice

MISSING = object()


def sign(x: int) -> int:
    if x == 0:
        return 0
    return -1 if x < 0 else 1


def range_2d(n: int, m: int) -> Iterable[tuple[int, int]]:
    for x in range(n):
        for y in range(m):
            yield x, y


def cells(matrix) -> Iterable:
    for x, row in enumerate(matrix):
        for y, v in enumerate(row):
            yield x, y, v


def batch(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def transpose[T](list2: list[list[T]]) -> list[list[T]]:
    return list(map(list, zip(*list2)))


def count[T](xs: Iterable[T], target: Callable[[T], bool] | T = MISSING) -> int:
    if target is MISSING:
        return sum(1 for x in xs)
    if isinstance(target, Callable):
        return sum(1 for x in xs if target(x))
    return sum(1 for x in xs if x == target)


def flatten[T](list2: Iterable[Iterable[T]]) -> list[T]:
    return [y for x in list2 for y in x]


def last[T](xs: Iterable[T]) -> T:
    result = None
    for x in xs:
        result = x
    return result


def sliding_window[T](xs: Iterable[T], n: int) -> tuple:
    iterator = iter(xs)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


def group_by(xs: Iterable, key: Callable) -> dict:
    r = defaultdict(list)
    for x in xs:
        r[key(x)].append(x)
    return r


def frequencies[T](xs: Iterable[T]) -> dict[T, int]:
    f = defaultdict(int)
    for x in xs:
        f[x] += 1
    return f


def get_submasks(mask: int) -> Iterable:
    x = mask
    while True:
        yield x
        if x == 0:
            break
        x = (x - 1) & mask


class DSU:
    def __init__(self, xs):
        self.sets = [[x] for x in xs]
        self.alive_set_ids = set(range(len(self.sets)))
        self.which = {x: i for i, x in enumerate(xs)}

    def get_set_id(self, x):
        return self.which[x]

    def same_set(self, x, y):
        return self.which[x] == self.which[y]

    def merge(self, x, y) -> bool:
        if self.same_set(x, y):
            return False

        left, right = self.which[x], self.which[y]
        if len(self.sets[left]) < len(self.sets[right]):
            left, right = right, left

        self.sets[left].extend(self.sets[right])
        for p in self.sets[right]:
            self.which[p] = left

        self.sets[right] = []
        self.alive_set_ids.remove(right)

        return True

    def __iter__(self):
        return iter(self.sets[id] for id in self.alive_set_ids)
