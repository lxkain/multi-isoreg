import timeit
import numpy as np

import mir


def create_shape(num: int=3,
                 minlen: int=2,
                 N: int=100):
    seq = np.empty(N)
    d = direction = int(np.random.rand(1) > 0.5) * 2 - 1
    inflection = sorted((np.random.permutation((N - 2 * minlen) // minlen) * minlen + minlen)[:num])

    seq[:inflection[0]] = d
    for i in range(len(inflection) - 1):
        d *= -1
        seq[inflection[i]:inflection[i+1]] = d
    seq[inflection[-1]:] = -d
    seq = np.cumsum(seq, dtype=np.float)
    return seq, direction, inflection


def print_inflection(seq, inflection):
    print(seq[:inflection[0]])
    for i in range(len(inflection) - 1):
        print(seq[inflection[i]:inflection[i+1]])
    print(seq[inflection[-1]:])

num = 5
minlen = 2
seq, direction, inflection = create_shape(num, minlen=minlen, N=64)
print(f"inflection = {inflection}")
print_inflection(seq, inflection)
print("------")
cmd = "mir.multi_isoreg(seq, num, direction=direction, minlen=minlen)"
if 0:  # profile
    print(timeit.timeit(cmd, globals=globals(), number=1))
else:  # see result
    err, inflection = eval(cmd)
    assert np.isclose(err, 0)
    print(f"error={err}")
    print(f"inflection = {inflection}")
    print_inflection(seq, inflection)
