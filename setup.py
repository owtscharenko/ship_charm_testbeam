# does gcc -Wall pat_c_send_and_cmd.c -o test -I/home/niko/ControlHost/include -L/home/niko/ControlHost/bin -lconthost
# libconthost_shared.so needs to be in pyproject folder regardless of what is written in library_dirs
# This setup relies on setuptools since distutils is insufficient and badly hacked code
import numpy as np
import os

from setuptools import setup, Extension, find_packages
from distutils.command.build_ext import build_ext
from Cython.Build import cythonize

version = '0.1.0'

extensions = [
    Extension("PyControlHost.control_host_coms", ["PyControlHost/ch_imports/control_host_coms.pyx"],
        include_dirs = ['../ControlHost/include', '../ControlHost/src'],
        libraries = ['conthost_shared'],) # library libconthost_shared.so must be in /usr/lib and accessable for user (chmod 0755)
#         library_dirs = ['/home/niko/git/ControlHost/bin'])
    ]

setup(
    name = "PyControlHost",
    version = version,
    packages = find_packages(),
    include_dirs = [np.get_include()], # needed on some systems to provided numpy c-library to compiler
    ext_modules = cythonize(extensions),
)