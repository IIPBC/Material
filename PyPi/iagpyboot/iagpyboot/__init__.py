# -*- coding:utf-8 -*-

""" IAG Python Boot Camp 2017 main module 
"""

import os as _os
import modules

__version__ = 0.3


def path():
    """ 
    :rtype: str
    :returns: The module path.

    :Example:

    >>> iagpyboot.hdtpath()
    /home/user/iagpyboot/
    """
    fulldir = _os.path.split(__file__)[0] + _os.path.sep
    end = 'iagpyboot' + _os.path.sep
    if not fulldir.endswith(end):
        fulldir += end
    return fulldir


if __name__ == '__main__':
    pass
