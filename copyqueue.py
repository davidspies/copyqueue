from flist import List
import flist


class Queue(object):
    def __init__(self, front=flist.EMPTY, back=flist.EMPTY):
        self._front = front
        self._back = back

    def push(self, x):
        self._front = flist.cons(x, self._front)
        self._try_topple()

    def _try_topple(self):
        if len(self._front) > len(self._back):
            self._back = self._back + reversed(self._front)
            self._front = List()

    def pop(self):
        (h, self._back) = self._back.uncons
        self._try_topple()
        return h

    def copy(self):
        return Queue(self._front, self._back)

    def __len__(self):
        return len(self._front) + len(self._back)
