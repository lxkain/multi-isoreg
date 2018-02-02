import timeit

import numpy as np

import mir

#np.random.seed(0)

def create_shape(num: int=3,
                 minlen: int=2,
                 N: int=100,
                 sigma: float=0):
    # TODO: check input validity
    seq = np.empty(N)
    direction = int(np.random.rand(1) > 0.5) * 2 - 1
    inflection = sorted((np.random.permutation((N - 2 * minlen) // minlen) * minlen + minlen)[:num])

    dir = direction  # local direction
    seq[:inflection[0]] = dir
    for i in range(len(inflection) - 1):
        dir *= -1  # reverse
        seq[inflection[i]:inflection[i+1]] = dir
    seq[inflection[-1]:] = -dir
    seq[:] = np.cumsum(np.r_[0, seq], dtype=np.float)[:-1]
    seq += np.random.randn(len(seq)) * sigma
    return seq, direction, inflection


def seq_inflection2subseq(seq, inflection):
    sub = []
    sub.append(seq[:inflection[0]])
    for i in range(len(inflection) - 1):
        sub.append(seq[inflection[i]:inflection[i+1]])
    sub.append(seq[inflection[-1]:])
    return sub


if __name__ == '__main__':
    P = 2
    num = P + (P - 1)
    N = 4
    minlen = 1
    seq, direction, inflection = create_shape(num, minlen=minlen, N=N, sigma=0.0)
    print(f"direction = {direction}")
    print(f"inflection = {inflection}")
    for i, s in enumerate(seq):
        print(f"{i:2} : {s} {'*' if i in inflection else ''}")
    print("------")

    # num = 2
    # minlen = 1
    # direction = -1
    # inf1 = [18, 19]
    # seq = [0. - 1. - 2. - 3. - 4. - 5. - 6. - 7. - 8. - 9. - 10. - 11. - 12. - 13. - 14.
    #        - 15. - 16. - 17. - 18. - 17. - 18.]

    if 1:
        if 0:  # profile
            print(timeit.timeit("mir.multi_isoreg(seq, num, direction=direction, minlen=minlen)", globals=globals(), number=1))
        else:  # see result
            err, inflection = mir.multi_isoreg(seq, num, direction=direction, minlen=minlen)
            print(f"error={err}")
            print(f"inflection = {inflection}")
            print(seq_inflection2subseq(seq, inflection))
