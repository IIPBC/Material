Modules, Packages, ``PyPi`` and all that...
*********************************************************************
Daniel Moser

Feb 15th, 2017

2nd IAG Python Boot Camp

.. contents:: Table of contents


Modules, Packages, and all that...
===================================
Python is a FREE language where simplicity matters. Thus, it should be easy to have (ie., download) published codes and also, publish your own code. 

Standardizing the names:

- **module** is Python code file containing definitions, functions, statements...
- **package** is a structure to share a set of modules.

This talk is complemented by this one: `from otherswork import wheel: looking for useful Python packages <http://danmoser.github.io/notes/import_wheel.html>`_.


How do I import a package in my code?
=======================================
.. code:: python

    import this

*Answer*: if you satisfy one of these 3 conditions:

- You are running ``python`` in the package's folder [*Bad!*]
- You explicitly asked python to look for it [*Okay, but not cool*]
- You properly installed it 

:: 

    Never run python from a package folder!


How do I properly install a Python package?
=============================================
*Answer*: one of two ways:

- ``python setup.py install`` (in the package main folder)
- using ``pip``!!!

pip
--------
"``pip`` *is a package management system used to install and manage software packages written in Python.*"

.. code:: bash

    pip install _package_
    # --user : local install (no admin rights)
    # -U or --upgrade : upgrade existing installation
    # --no-deps : no install of dependencies packages (useful for upgrade)
    # --install-option="--prefix=$PREFIX_PATH" redirects the install

``pip`` in embedded in 2.7.9+. If you have an updated version of Python and don't find it, run this command:

.. code:: bash

    python -m ensurepip

Remember: ``pip`` installs binaries in addition to the modules. Add this installation path to your `$PATH` (in unix, is is `$HOME/.local/bin`).

**WARNING**: *Never* combine ``sudo`` with ``--user``! Otherwise you will face critical permission problems for your packages!

:: 

    Many more from pip can be learned!


Where do ``pip`` look for packages?
=====================================
*Answer*: In the Python Package Index: ``PyPi``!!!

"The Python Package Index *(aka ``PyPI`` -- formerly known as the "Cheese Shop") is the preferred hub for publishing Python packages and modules. Python's standard library supports code uploads to PyPI through its ``distutils`` module."*

https://pypi.python.org or http://cheeseshop.python.org


How do I publish in the ``PyPi``??
====================================
*Answer*: do this check list:

- Make sure you know how to build a module.
- Make sure your code is working.
- Make sure your revised your code with good programming practices (coding style, documentation [with examples], compatibility between versions, unit testing...)
- Generate a compatible ``setup.py`` file.
- Test it uploading to ``testPyPi``.
- Upload it to ``PyPi``.

:: 

    This check list is not to discourage you. 
    It's to encourage you to do these things, because in the long run 
    they really are worth it (believe me!)


How a build a module?
=======================
That's a very good question!

Look the ``iagpyboot`` module example! (It should be at https://github.com/IIPBC/Material ...)


How do I generate a ``setup.py`` compatible with ``PyPi``?
==============================================================================
Here you have a MWE (minimal working example):

.. code:: python

    #!/usr/bin/env python
    # -*- coding:utf-8 -*-

    """ Writing the Setup Script

     https://docs.python.org/2/distutils/setupscript.html
    """

    from setuptools import setup  # , find_packages
    # from distutils.core import setup

    setup(name='iagpyboot',
          version='0.2',
          description='IAG Python Boot Camp example',
          author='Daniel Moser',
          author_email='moser@usp.br',
          url='http://iagpyboot.wixsite.com/pbc2017',
          packages=['iagpyboot'],
          )


How do I upload to ``TestPyPi``?
======================================
*Answer*: **Read** `Test PyPi Server <https://wiki.python.org/moin/TestPyPI>`_!

1. Register with the site. It has a different user database than the main PyPI server. It also gets cleaned out on a semi-regular basis.

2. Fill in your test PyPI credentials in your ~/.pypirc file. You should end up with something like this:

.. code::

    [distutils]
    index-servers=
        pypi
        testpypi

    [testpypi]
    repository = https://testpypi.python.org/pypi
    username = iagpyboot
    password = IAGpbc2017

    [pypi]
    repository = https://pypi.python.org/pypi
    username = <your user name goes here>
    password = <your password goes here>

3. Go to your project ``setup.py`` folder. Use the test server URL to register your project (it gives you the right to modify your project on the server):

.. code:: bash

   python setup.py register -r https://testpypi.python.org/pypi

4. Then uploading it: 

.. code:: bash

    python setup.py sdist upload -r https://testpypi.python.org/pypi

5. Test it acessing https://testpypi.python.org/pypi/iagpyboot !!!


How do I install my package from ``TestPyPi``?
=================================================
*Answer*: Once your project is on the server, test that you can install your package from ``TestPyPi``:

.. code:: bash

    pip install -i https://testpypi.python.org/pypi <package name>


Final remark
==============
Good luck publishing your code!
