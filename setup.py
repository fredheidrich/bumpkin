"""
"""

import os
import sys
import setuptools


version_file = "VERSION"
if os.path.exists(version_file):
    with open(version_file, "r") as file:
        __version__ = file.read().strip()
else:
    __version__ = "2021.8"


setuptools.setup(
 name="standard-bumpkin",
 py_modules="bumpkin",
 author="Fred Heidrich",
 version=__version__,
 classifiers = [
     "Programming Language :: Python",
     "Programming Language :: Python :: 3",
     "Programming Language :: Python :: 3.7",
     "Development Status :: 3 - Alpha",
     # "Development Status :: 4 - Beta",
     # "Development Status :: 5 - Production/Stable",
     "Environment :: Other Environment",
     "Intended Audience :: Developers",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
     "Topic :: Software Development :: Pre-processors",
     "Topic :: Software Development :: Libraries :: Python Modules",
     "Topic :: Software Development :: Code Generators",
 ]
)

