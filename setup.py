#from Cython.Distutils import setup
#(...needed to install setuptools via pip rather than use cython.distutils...)


from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("CythonTest.pyx"))

# STEP 1 - To build this run "python setup.py build_ext --inplace" from the terminal (don't run from within VS Code)
# STEP 2 - Needed to put the path to "python.h" in the includepath of VS code with ctrl+shift+P and "C/C++ edit configuration(UI)"
# STEP 3 - To compile the C file output from step 1, use the VS 2022 Developer PS and run "cl CythonTest.c"