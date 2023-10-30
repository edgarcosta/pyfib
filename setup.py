#!/usr/bin/env python
## -*- encoding: utf-8 -*-

import os
import sys
from setuptools import setup
from codecs import open  # To open the README file with proper encoding
from setuptools.command.test import test as TestCommand  # for tests
from setuptools.extension import Extension

# Get information from separate files (README, VERSION)
def readfile(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()


# For the tests
class SageTest(TestCommand):
    def run_tests(self):
        errno = os.system("sage -t --force-lib pyfib")
        if errno != 0:
            sys.exit(1)


cythonize_dir = "build"

from Cython.Build import cythonize as cython_cythonize

try:
    from sage.misc.package_dir import cython_namespace_package_support
    def cythonize(*args, **kwargs):
        with cython_namespace_package_support():
            return cython_cythonize(*args, **kwargs)
except ImportError:
    cythonize = cython_cythonize



fib = Extension(
    "pyfib.fib",
    language="cython",
    sources=[
        "pyfib/fib.pyx"
    ],
)

setup(
    name="pyfib",
    author="Edgar Costa",
    author_email="edgarc@mit.edu",
    url="https://github.com/edgarcosta/pyfib",
    license="GNU General Public License, version 3",
    description='Sage code ...',
    long_description=readfile("README.md"),  # get the long description from the README
    version=readfile("VERSION").strip(),  # the VERSION file is shared with the documentation
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: GNU General Public License, version 3",
        "Programming Language :: Python :: 3.7",
    ],  # classifiers list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="sagemath pyfib",
    setup_requires=[
        "cython",
        "sagemath",
    ],  # currently useless, see https://www.python.org/dev/peps/pep-0518/
    install_requires=[
        "cython",
        "sagemath",
        "sphinx",
    ],
    packages=["pyfib"],
    include_package_data=False,
    ext_modules=cythonize([fib]),
    cmdclass={"test": SageTest}  # adding a special setup command for tests
    # ext_modules = extensions,
    # cmdclass = {'test': SageTest, 'build_ext': Cython.Build.build_ext} # adding a special setup command for tests and build_ext
)
