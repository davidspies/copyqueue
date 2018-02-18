class Queue(object):
    def __init__(self, q=None):
        if q is None:
            self._q = []
        else:
            self._q = q

    def push(self, x):
        self._q.append(x)

    def pop(self):
        return self._q.pop(0)

    def copy(self):
        return Queue(list(self._q))

    def __len__(self):
        return len(self._q)
