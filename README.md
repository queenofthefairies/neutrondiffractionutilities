Neutrondiffractionutilities extension to xrayutilities
=============
# About neutrondiffractionutilities
I am modifying the original xrayutilities package for neutron diffraction experiments

* specifically single crystals     
* mounted on an Eulerian cradle (4 circles total, 3 sample + 1 detector rotation axes)   
* continuous wave source
* large area detector
* Wombat instrument at ANSTO's Australian Centre for Neutron Scattering

# About xrayutilities

[![Build Status](https://dev.azure.com/dominikkriegner/xrayutilities/_apis/build/status/dkriegner.xrayutilities?repoName=dkriegner%2Fxrayutilities&branchName=main)](https://dev.azure.com/dominikkriegner/xrayutilities/_build/)

xrayutilities is a collection of scripts used to analyze and simulate x-ray
diffraction data.  It consists of a Python package and several routines coded
in C. For analysis the package is especially useful for the reciprocal space
conversion of diffraction data taken with linear and area detectors. For
simulations code for X-ray reflectivity, kinematical and dynamical diffraction
simulation of crystal truncation rods as well as fundamental parameters powder
diffraction is included.


Copyright (C) 2009-2025 Dominik Kriegner <dominik.kriegner@gmail.com>

Copyright (C) 2009-2013 Eugen Wintersberger <eugen.wintersberger@desy.de>


Mailing list and issue tracker
------------------------------

To get in touch with us or report an issue please use the mailing list
(https://sourceforge.net/p/xrayutilities/mailman/xrayutilities-users/) or the
Github issue tracker (https://github.com/dkriegner/xrayutilities/issues). When
you want to follow announcements of major changes or new releases its
recommended to [sign up for the mailing
list](https://sourceforge.net/projects/xrayutilities/lists/xrayutilities-users)


Contents
--------

* *doc*:                documentation source files
* *examples*:           directory with example scripts and configurations
* *lib/xrayutilities*:  directory with the sources for the Python package
* *src*:                directory with the C extension for improved performance
* *tests*:              directory with the unittest scripts
* *pyproject.toml, meson\**: packaging configuration and build files


Installation (pip)
==================
Using the python package manager pip you can install xrayutilities by executing

    pip install xrayutilities

Installation (source)
=====================
Installing xrayutilities from source is an easy process done by executing

    pip install .

By default the installation procedure enables OpenMP support (recommended).
It fails if no OpenMP support is available. It can be disabled by using the
the following custom meson option for the installation:

    pip install . --config-settings=setup-args="-Duse_openmp=disabled"

To allow to proceed with the installation without OpenMP but use it if available use:

    pip install . --config-settings=setup-args="-Duse_openmp=auto"

Requirements
------------
The following requirements are needed for installing and using *xrayutilities*:

- Python (>= 3.6)
- h5py
- scipy (version >= 0.18.0)
- numpy (version >= 1.9, >2.0 since xrayutilities-1.7.8)
- lmfit (>= 1.0.1)
- matplotlib (optional, version >= 3.1.0)
- mayavi (optional, only used optionally in `Crystal.show_unitcell`)

When building from source you also might need:

- C-compiler (with OpenMP support)
- Python dev headers
- meson-python
- pytest (optional - only if you want to run the test environment)
- sphinx (optional - only when you want to build the documentation)
- numpydoc (optional - only when you want to build the documentation)
- rst2pdf (optional - only when you want to build the documentation)
- sphinx_rtd_theme (optional - only when you want to build the documentation)
- sphinx-pyproject (optional - only when you want to build the documentation)
- svglib (optional - only when you want to build the pdf documentation)

refer to your operating system documentation to find out how to install
those packages. On Microsoft Windows refer to the Documentation for the
easiest way of the installation (Anaconda, Python(x,y), or WinPython).

Python-2.7 and Python-3.X compatibility
=======================================

The current development is for Python3 (version >=3.6) only. xrayutilities up
to version 1.5.x can be used with Python-2.7 as well. Python 3.3 to 3.5 was
supported up to 1.6.0.

The Python package configuration
================================

The following steps should only be necessary when using non-default
installation locations to ensure the Python module is found by the Python
interpreter. In this case the module is installed under
*<prefix>/lib[64]/python?.?/site-packages* on Unix systems and
*<prefix>/Lib/site-packages* on Windows systems.

If you have installed the Python package in a directory unknown to your Python
distribution, you have to tell Python where to look for the Package.  There are
several ways how to do this:

- add the directory where the package is installed to your
  *PYTHONPATH* environment variable.

- add the path to sys.path in the *.pythonrc* file placed in your home
  directory

      import sys
      sys.path.append("path to the xrayutilities package")

- simply apply the previous method in every script where you want to
  use the xrayutilities package before importing the package

      import sys
      sys.path.append("path to the xrayutilities package")
      import xrayutilities

Obtaining the source code
=========================

The sources are hosted on sourceforge in git repository.
Use

    git clone https://github.com/dkriegner/xrayutilities.git

to clone the git repository. If you would like to have commit rights
contact one of the administrators.

Update
======

if you already installed xrayutilities you can update it by navigating into
its source folder and obtain the new sources by ::

    git pull

or download the new tarball from sourceforge
(https://sf.net/projects/xrayutilities) if any code changed during the update you
need to reinstall the Python package. Thats easiest achieved by

    pip install .

In case you are not certain about the installation location it can be determined by

    python -c "import xrayutilities as xu; print xu.__file__"
      /usr/local/lib64/python3.6/site-packages/xrayutilities/__init__.pyc

if the output is e.g.: */usr/local/lib64/python3.6/site-packages/xrayutilities/__init__.py*
you previously installed xrayutilities in */usr/local*, which should be used
again as install path. Use ::

    pip install --prefix=<path to install directory> .

to install the updated package.


Documentation
=============

Documentation for xrayutilities is found on the webpage
https://xrayutilities.sourceforge.io

The API-documentation can also be browsed by

    pydoc -p PORT

in any web-browser, after the installation is finished.
