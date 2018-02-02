import cython
from cython.view cimport array as cvarray
import numpy as np
cimport numpy as np
from numpy import r_, array as nparray

from mir_c cimport isotonic_regression


@cython.boundscheck(False)
@cython.wraparound(False)
cdef _multi_isoreg(double *seq,
                   unsigned n,
                   unsigned num,
                   signed direction,
                   unsigned minlen,
                   double *hat):
    cdef double err_left, err_rite, mine
    cdef unsigned i, index, size, arg
    I = n - minlen * num + 1 - minlen
    cdef double[:] err = cvarray(shape=(I,), itemsize=sizeof(double), format="d")
    opt = [0] * I  # needs to be local
    for i in range(I):
        index = i + minlen
        # left side
        err_left = isotonic_regression(seq, hat, index, direction)
        size = n - index
        # right side, reverse direction
        if num > 1:  # split further
            err_rite, subopt = _multi_isoreg(seq + index, size, num - 1, -direction, minlen, hat)
            opt[i] = subopt + index
        else:  # no more inflection points
            err_rite = isotonic_regression(seq + index, hat, size, -direction)
            opt[i] = None
        err[i] = err_left + err_rite
    mine = err[0]
    arg = 0
    for i in range(1, I):
        if err[i] < mine:
            mine = err[i]
            arg = i
    return mine, r_[minlen + arg, opt[arg]] if opt[arg] is not None else nparray([minlen + arg])


def multi_isoreg(seq: np.ndarray,
                 num: int,
                 direction: int=1,
                 minlen: int=2): # -> (float, np.ndarray):
    """
    Multiple Isotonic Regression

    :param seq: input sequence
    :param num: number of inflection points to be detected
    :param direction: 1 if first segment is expected to go up, -1 if down
    :param minlen: minimum separation between inflection points
    :return: (minimum_error, inflection_points)
    """
    def check_ndarray(obj):
        assert (obj.flags.c_contiguous or obj.flags.f_contiguous), "must have contiguous storage"
        assert obj.flags.aligned, "must be aligned"

    if minlen < 2:
        raise NotImplementedError('for now, minlen must be > 1')
    hat : np.ndarray = np.empty_like(seq)  # allocate scratch space
    for obj in [seq, hat]:
        check_ndarray(obj)
    return _multi_isoreg(<double *>seq.data, seq.shape[0], num, direction, minlen, <double *>hat.data)


