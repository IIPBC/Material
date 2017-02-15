iagpyboot
===========
**II IAG Python Boot Camp module example**.


How to install/uninstall
--------------------------
You should know that...

.. warning::

    Never combine ``sudo`` with ``--user``! Otherwise you will face critical permission problems for your packages!

.. note:: 

    To use the scripts, the binaries path of your pip installation directory must be in system ``PATH``. If you don't find them, adapt the following command to your ``$HOME/.bashrc``:

    .. code:: bash

        PATH=$PATH:~/.local/bin/


To only **update** the package:

.. code:: bash

    pip install -U --no-deps <package name>

``-U`` forces the upgrade and ``--no-deps`` do not reinstall the dependent packages. 


How to use the modules
-------------------------
To make use of all routines, the suggestion is to import them as follows:

.. code:: python

    import iagpyboot as pbc
    

License
-----------
The code is free, available under the terms of the "GNU GPL v3.0 license".
