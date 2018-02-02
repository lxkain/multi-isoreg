from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import Cython.Compiler.Options

import numpy as np

Cython.Compiler.Options.annotate = False

extensions = [
    Extension("mir", ["mir.pyx", "mir_c.c"],
              include_dirs=[np.get_include()],
              extra_compile_args=['-w']),
]

if 1:
    setup(
        ext_modules=cythonize(extensions)
    )
