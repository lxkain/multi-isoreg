import timeit

import numpy as np

import mir


def create_shape(num: int=3,
                 minlen: int=2,
                 N: int=100,
                 sigma: float=0):
    seq = np.empty(N)
    direction = int(np.random.rand(1) > 0.5) * 2 - 1
    inflection = sorted((np.random.permutation((N - 2 * minlen) // minlen) * minlen + minlen)[:num])

    seq[:inflection[0]] = direction
    for i in range(len(inflection) - 1):
        direction *= -1
        seq[inflection[i]:inflection[i+1]] = direction
    seq[inflection[-1]:] = -direction
    seq[:] = np.cumsum(seq, dtype=np.float)
    seq += np.random.randn(len(seq)) * sigma
    return seq, direction, inflection


def print_inflection(seq, inflection):
    print(seq[:inflection[0]])
    for i in range(len(inflection) - 1):
        print(seq[inflection[i]:inflection[i+1]])
    print(seq[inflection[-1]:])


num = 5
minlen = 2
seq, direction, inflection = create_shape(num, minlen=minlen, N=64, sigma=0.0)
print(f"inflection = {inflection}")
print(seq)
print("------")
cmd = ""
if 0:  # profile
    print(timeit.timeit("mir.multi_isoreg(seq, num, direction=direction, minlen=minlen", globals=globals(), number=1))
else:  # see result
    err, inflection = mir.multi_isoreg(seq, num, direction=direction, minlen=minlen)
    print(f"error={err}")
    print(f"inflection = {inflection}")
    print_inflection(seq, inflection)
