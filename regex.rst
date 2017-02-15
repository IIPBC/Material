Regular expressions (*re* ou *regex*)
#############################################
(**Expressões regulares**)

Daniel Moser

Feb 15th, 2017

2nd IAG Python Boot Camp

.. contents:: Table of contents

Preliminaries
==============
.. figure:: ../figs/regex-raiznutella.png
    :align: center
    :width: 640 px

=============================== ==============================
Pythonista raiz                 Pythonista nutella
=============================== ==============================
Segue PEP8                      Estilo é o do momento
Usa ``docstrings``              Comenta com *#*
Usa editor de texto             Usa *PyCharm*
Testa código no ``ipython``     Usa *Jupyter/Notebook*
Codifica em OOP                 Codifica em procedural
Usa ``regex``                   Manipula strings como ``str``  
Publica código no ``PyPi``      Publica código no *github*
=============================== ==============================

Basics
==========
A **regular expression** is a sequence of characters that define a **search pattern**. In other words, is a specific textual syntax for representing patterns that a matching text need to conform to.

Must read: Paulo Penteado's talk `Processing strings (PDF) <http://dl.dropbox.com/u/6569986/gai/pp_cc_strings.pdf>`_

And.. *Read the Docs*! 
    - https://docs.python.org/2/library/re.html
    - https://docs.python.org/3/library/re.html

- regex recognizes special characters with ``"\"`` (example: ``\n, \t``).
- ``.`` any character, but new line.  If the *DOTALL* flag has been specified, this matches any character including a newline.
- ``^`` beginning of a string. In Python *MULTILINE* mode, the beginning of a line
- ``$`` end of a string or before the end of a line
- ``*`` many occurrences 
- ``+`` one or more occurrences
- ``?`` 0 or 1 occurrence
- ``{m}`` the exact pattern *m*-times
- ``{m,}`` the exact pattern *m* or more times
- ``{m,n}`` the exact pattern between *m* and *n* times
- ``{,n}`` the exact pattern *n* or less times
- ``\w`` Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9\_].
- ``\W`` Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9\_].
- ... many, many more.


Examples
==========
From Wikipedia:
-----------------
Text to be working over::

    "at", "bat", "cat", "hat", "[rat]", "dog";
    "at", "ccat", "chat", "hcat", "hhat", "s", "saw", "seed".

Regex: 

- ``.at`` matches any three-character string ending with "at", including "hat", "cat", and "bat".

- ``[hc]at`` matches "hat" and "cat".

- ``[^b]at`` matches all strings matched by .at except "bat".

- ``[^hc]at`` matches all strings matched by .at other than "hat" and "cat".

- ``^[hc]at`` matches "hat" and "cat", but only at the beginning of the string or line.

- ``[hc]at$`` matches "hat" and "cat", but only at the end of the string or line.

- ``\[.\]`` matches any single character surrounded by "[" and "]" since the brackets are escaped, for example: "[a]" and "[b]".

- ``s.*`` matches s followed by zero or more characters, for example: "s" and "saw" and "seed".

- ``[hc]+at`` matches "hat", "cat", "hhat", "chat", "hcat", "cchchat", and so on, but not "at".

- ``[hc]?at`` matches "hat", "cat", and "at".

- ``[hc]*at`` matches "hat", "cat", "hhat", "chat", "hcat", "cchchat", "at", and so on.

- ``cat|dog`` matches "cat" or "dog".
 

Others
-----------
- ``[^\s]+`` returns a word until the first space/empty character.

- ``^\"(?!.*s.*).*`` returns all line content starting with ``"`` and that *do not* contain the letter "s" (case sensitive); *MULTILINE* mode.


Online testers
================
Choose one (or several)!!

- https://regex101.com
- http://www.regexpal.com
- http://regex.larsolavtorvik.com
- http://www.nregex.com
- http://www.rubular.com
- http://www.myregexp.com


Python
=========
- ``re``: built-in regex module
- ``regex``: third-part regex module (a bit more features)

Python examples
------------------
.. code:: python

    """Split example"""

    import re

    regex = re.compile(r'\W+')
    regex.split('This is a test, short and sweet, of split().')


.. code:: python

    """Substitution example"""
    
    def start_case_words(s):
        """ Function to put a string in Start Case. 
        
        It can by vectorized by numpy: ``vecstart = np.vectorize(start_case_words) """
        return re.sub(r'\w+', lambda m:m.group(0).capitalize(), s)


.. code:: python

    """All matches examples"""

    rule = r'^>([^\n\r]+)[\n\r]([A-Z\n\r]+)'

    regex = re.compile(rule, re.MULTILINE)
    matches0 = []
    for m in regex.finditer(text):
        matches0.append(m.groups())
    
    # for m in matches0:
    #     print 'Name: %s\nSequence:%s' % (m[0], m[1])

    # Other way
    regex = re.compile(rule, re.MULTILINE)
    matches1 = [m.groups() for m in regex.finditer(text)]

    # Other way (MUCH better):
    regex = re.compile(rule, re.MULTILINE)
    matches2 = re.findall(rule, text)  

    # Another:
    regex = re.compile(rule, re.MULTILINE)
    matches3 = re.compile(rule, re.MULTILINE).findall(text)


Good references
===================
- http://overapi.com/regex
- https://docs.python.org/2/library/re.html
- https://docs.python.org/2/howto/regex.html
- http://www.tutorialspoint.com/python/python_reg_expressions.htm

Exercise
===========
1. From the text below:

- a) Retrieve all lines that contains the word "better".
- b) Count the length of each sentence (in words).

::

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


2. Create a dictionary in which the keys are the acronyms of the USP institutes and the values the complete name. You **must** use ``regex``!

:: 

    Escola de Artes, Ciências e Humanidades (EACH)
    Escola de Comunicações e Artes (ECA)
    Escola de Educação Física e Esporte (EEFE)
    Escola de Enfermagem (EE)
    Escola Politécnica (Poli)
    Faculdade de Arquitetura e Urbanismo (FAU)


..  
    "Best" solution:

    rule = r"^(.*)\((.*)\)"

    Alternative:

    MULTILINE mode
    rule_vals = r'^(.*?)\('
    rule_keys = r'\((.*)\)'

    regex = re.compile(rule, re.MULTILINE)
    matches = [m.groups() for m in regex.finditer(text)]
