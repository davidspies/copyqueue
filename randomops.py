from copyqueue import Queue
import random

PUSH = 'u'
POP = 'o'
COPY = 'c'

OPS = ''.join((k * v for (k, v) in {POP: 1, PUSH: 1, COPY: 1}.items()))


def run_operations(n, qconstr=Queue):
    state = random.getstate()
    count_arr = [0]

    def do_ops(qconstr):
        random.setstate(state)
        q = qconstr()
        q.push(-1)
        qs = [q]
        k = 5
        largest_k_qs = [q]

        def check_replace_largest_k(qr):
            if qr not in largest_k_qs:
                if len(largest_k_qs) < k:
                    largest_k_qs.append(qr)
                else:
                    smallest_largest = min(
                        range(k), key=lambda j: len(largest_k_qs[j]))
                    if len(largest_k_qs[smallest_largest]) < len(qr):
                        largest_k_qs[smallest_largest] = qr

        for i in range(n):
            if random.random() > 0.5:
                qr = random.choice(qs)
            else:
                qr = random.choice(largest_k_qs)
            op = random.choice(OPS)
            if op == PUSH:
                qr.push(i)
                check_replace_largest_k(qr)
            elif op == COPY:
                qs.append(qr.copy())
            elif op == POP:
                qr.push(i)
                yield qr.pop()
        count_arr[0] = sum(len(q) for q in qs)

    result = list(do_ops(qconstr))
    return (do_ops, result, count_arr[0])
