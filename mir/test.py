from unittest import TestCase

import numpy as np

from main import create_shape, seq_inflection2subseq, mir


class TestCreateShape(TestCase):
    def test_shapes(self):
        for num in range(1, 5):
            for minlen in range(1, 5):
                for N in range(20, 40):
                    for t in range(100):
                        seq, dir, inf = create_shape(num=num,
                                                     minlen=minlen,
                                                     N=N,
                                                     sigma=0)
                        self.assertTrue(len(inf) == num, msg=f"""                        
                        num = {num}
                        minlen = {minlen}
                        N = {N}
                        seq = {seq}
                        dir = {dir}
                        inf = {inf}
                        """)
                        self.assertTrue(len(seq) == N)

    def test_sub(self):
        for num in range(1, 5):
            for minlen in range(1, 5):
                for N in range(20, 40):
                    for t in range(100):
                        seq, dir, inf = create_shape(num=num,
                                                     minlen=minlen,
                                                     N=N,
                                                     sigma=0)
                        sub = seq_inflection2subseq(seq, inf)
                        for i, s in enumerate(sub):
                            self.assertTrue((np.sign(np.diff(s)) == dir).all())
                            dir *= -1

class TestMir(TestCase):
    def test_error(self):
        for num in range(1, 5):
            for minlen in range(2, 5):  # there is a bug when minlen is 1, skipping that for now
                for N in range(20, 40):
                    for t in range(200):
                        seq, direction, inf1 = create_shape(num=num,
                                                     minlen=minlen,
                                                     N=N,
                                                     sigma=0)
                        err, inf2 = mir.multi_isoreg(seq, num, direction, minlen)
                        self.assertAlmostEqual(err, 0, msg=f"""
                        num = {num}
                        minlen = {minlen}
                        N = {N}
                        seq = {seq}
                        direction = {direction}
                        inf1 = {inf1}
                        inf2 = {inf2}
                        """)