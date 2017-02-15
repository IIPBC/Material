#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" Writing the Setup Script

 https://docs.python.org/2/distutils/setupscript.html
"""

from setuptools import setup  # , find_packages
# from distutils.core import setup

setup(name='iagpyboot',
      version='0.3',
      description='IAG Python Boot Camp example',
      author='Daniel Moser',
      author_email='moser@usp.br',
      url='http://iagpyboot.wixsite.com/pbc2017',
      packages=['iagpyboot'],
      )
