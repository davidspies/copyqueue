class List(object):
    def __init__(self, uncons=None, length=0):
        self._uncons = uncons
        self._pr = None
        self._len = length

    @property
    def uncons(self):
        if self._uncons is not None:
            self._pr = self._uncons()
            self._uncons = None
        return self._pr

    @property
    def head(self):
        return self.uncons[0]

    @property
    def tail(self):
        return self.uncons[1]

    def __add__(self, other):
        def uncons():
            if self.uncons is None:
                return other.uncons
            else:
                h, t = self.uncons
                return h, t + other
        return List(uncons, len(self) + len(other))

    def __iter__(self):
        x = self
        while x.uncons is not None:
            h, x = x.uncons
            yield h

    def __len__(self):
        return self._len

    def __reversed__(self):
        return lazy(
            (lambda: from_gen(reversed(list(self)), len(self))), len(self))


def from_gen(g, length):
    it = iter(g)

    def uncons():
        try:
            h = next(it)
        except StopIteration:
            return None
        return (h, from_gen(it, length - 1))
    return List(uncons, length)


def from_list(l):
    return from_gen(l, len(l))


def lazy(f, length):
    return List((lambda: f().uncons), length)


def cons(hd, tl):
    return List(lambda: (hd, tl), len(tl) + 1)


EMPTY = List()
