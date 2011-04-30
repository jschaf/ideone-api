===================
 Ideone Python API
===================

`Ideone`_ is a pastebin, as well as an online compiler and debugger.
This project is a Pythonic binding to the `Ideone API`_. 

Installation
============

The Ideone API can also be installed with ``pip`` from `PyPI`_ using
``pip install ideone``.  Alternately, you can clone the repository and
use setup.py like so ::

    git clone https://github.com/jschaf/ideone-api.git
    cd ideone-api
    python setup.py install

Getting Started
===============

You need an Ideone account and an *API password* which you can create
at the `Ideone registration page`_.  After that, open up a Python
shell and begin hacking. ::

    >>> from ideone import Ideone
    >>> i = Ideone('username', 'APIpassword')
    >>> i.test()
    {'answerToLifeAndEverything': 42,
     'error': "OK",
     'moreHelp': "ideone.com",
     'oOok': True,
     'pi': 3.14}

    >>> i.create_submission('print(42)', 'python')
    {'error': 'OK',
     'link' : 'LsSbo'}

    >>> i.submission_details('LsSbo')
    {'cmpinfo': "",
     'date': "2011-04-18 15:24:14",
     'error': "OK",
     'input': "",
     'langId': 116,
     'langName': "Python 3",
     'langVersion': "python-3.1.2",
     'memory': 5852,
     'output': 42,        
     'public': True,
     'result': 15,
     'signal': 0,
     'source': "print(42)",
     'status': 0,
     'stderr': "",
     'time': 0.02}

    >>> i.languages()
    {'error': 'OK',
    'languages': {1: "C++ (gcc-4.3.4)",
                  2: "Pascal (gpc) (gpc 20070904)",
                  ...
                  ...
                  ...
                  125: "Falcon (falcon-0.9.6.6)"}}


.. _ideone: http://ideone.com
.. _Ideone API: http://ideone.com/api
.. _PyPI: http://pypi.python.org/pypi/ideone
.. _Ideone registration page: http://ideone.com/account/register

