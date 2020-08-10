rockstar-py
===========

.. raw:: html

    <h2 align="center">Python transpiler for the esoteric language <a href="https://github.com/dylanbeattie/rockstar">Rockstar</a></h2>

    <p align="center">
    <a href="https://travis-ci.com/yyyyyyyan/rockstar-py"><img src="https://img.shields.io/travis/yyyyyyyan/rockstar-py" alt="Travis (.org)"></a>
    <a href="https://pypi.org/project/rockstar-py"><img src="https://img.shields.io/pypi/v/rockstar-py" alt="PyPI - Version"></a>
    <a href="https://pypi.org/project/rockstar-py"><img src="https://img.shields.io/pypi/status/rockstar-py" alt="PyPI - Status"></a>
    <a href="https://pepy.tech/project/rockstar-py"><img src="https://pepy.tech/badge/rockstar-py" alt="PyPI - Status"></a>
    <a href="https://pypi.org/project/rockstar-py"><img src="https://img.shields.io/pypi/pyversions/rockstar-py" alt="PyPI - Python Version"></a>
    <a href="https://pypi.org/project/rockstar-py"><img src="https://img.shields.io/pypi/wheel/rockstar-py" alt="PyPI - Wheel"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style - Black"></a>
    <a href="https://github.com/yyyyyyyan/rockstar-py/graphs/contributors"><img src="https://img.shields.io/github/contributors/yyyyyyyan/rockstar-py" alt="GitHub contributors"></a>
    <a href="https://github.com/yyyyyyyan/rockstar-py/stargazers"><img src="https://img.shields.io/github/stars/yyyyyyyan/rockstar-py" alt="GitHub stars"></a>
    <a href="https://github.com/yyyyyyyan/rockstar-py"><img src="https://img.shields.io/github/languages/code-size/yyyyyyyan/rockstar-py" alt="GitHub code size in bytes"></a>
    <a href="https://github.com/yyyyyyyan/rockstar-py/blob/master/LICENSE.txt"><img src="https://img.shields.io/github/license/yyyyyyyan/rockstar-py" alt="License - MIT"></a>
    </p>

Getting Started
---------------

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes.

Installing
~~~~~~~~~~

First, make sure you have installed a supported Python version (>= 3.5).

Now, the easiest way of installing **rockstar-py** is using pip:

::

    pip install rockstar-py

(This may require ``sudo`` if you're installing globally on a \*nix system.

You can also clone this project using git and install the package with setuptools:

::

    git clone https://github.com/yyyyyyyan/rockstar-py.git
    cd rockstar-py
    python3 setup.py install

Usage
-----

If you installed the package using pip or setuptools, you can simply run rockstar-py in the command line:

::

    rockstar-py [-h] (-i INPUT | --stdin) [-o OUTPUT | --stdout | --exec] [-v]

Otherwise, you can run the transpiler from inside the ``rockstar-py`` folder by calling python with the ``-m`` flag:

::

    python3 -W ignore -m rockstarpy [-h] (-i INPUT | --stdin) [-o OUTPUT | --stdout | --exec] [-v]

Call ``rockstar-py`` with the flag ``-h``/``--help`` to see a description of all options:

::

    usage: rockstar-py [-h] (-i INPUT | --stdin) [-o OUTPUT | --stdout | --exec] [-v]

    Python transpiler for the esoteric language Rockstar

    optional arguments:
     -h, --help            show this help message and exit
     -i INPUT, --input INPUT
                           Input file (.rock)
     --stdin               Stream in stdin
     -o OUTPUT, --output OUTPUT
                           Output file (.py)
     --stdout              Stream to stdout
     --exec                Execute (without saving) the transpiled code
     -v, --version         Version

Examples
--------

Just to make it more clear, some examples with the `fizz.rock`_ code.

Basic usage
~~~~~~~~~~~

::

    > rockstar-py -i fizz.rock -o fizz.py
    > ls
    fizz.py  fizz.rock
    > cat fizz.py
    def Midnight(your_heart, your_soul):
       while your_heart >= your_soul: # this is a comment
           your_heart = your_heart - your_soul
       return your_heart
    Desire = 100
    my_world = False
    Fire = 3 # i love comments
    Hate = 5
    while not my_world == Desire:
       my_world += 1
       if Midnight(my_world, Fire) == False and Midnight(my_world, Hate) == False:
           print("FizzBuzz!")
           continue
       if Midnight(my_world, Fire) == False:
           print("Fizz!")
           continue
       if Midnight(my_world, Hate) == False:
           print("Buzz!")
           continue
       print(my_world)

Using ``--stdout``
~~~~~~~~~~~~~~~~~~

::

    > rockstar-py -i fizz.rock --stdout
    def Midnight(your_heart, your_soul):
       while your_heart >= your_soul: # this is a comment
           your_heart = your_heart - your_soul
       return your_heart
    Desire = 100
    my_world = False
    Fire = 3 # i love comments
    Hate = 5
    while not my_world == Desire:
       my_world += 1
       if Midnight(my_world, Fire) == False and Midnight(my_world, Hate) == False:
           print("FizzBuzz!")
           continue
       if Midnight(my_world, Fire) == False:
           print("Fizz!")
           continue
       if Midnight(my_world, Hate) == False:
           print("Buzz!")
           continue
       print(my_world)

Using ``--stdin``
~~~~~~~~~~~~~~~~~

::

    > rockstar-py --stdin -o fizz.py
    Midnight takes your heart and your soul
    While your heart is as high as your soul (this is a comment)
    Put your heart without your soul into your heart

    Give back your heart


    Desire's a lovestruck ladykiller
    My world is empty
    Fire's ice (i love comments)
    Hate is water
    Until my world is Desire,
    Build my world up
    If Midnight taking my world, Fire is nothing and Midnight taking my world, Hate is nothing
    Shout "FizzBuzz!"
    Take it to the top

    If Midnight taking my world, Fire is nothing
    Shout "Fizz!"
    Take it to the top

    If Midnight taking my world, Hate is nothing
    Say "Buzz!"
    Take it to the top

    Whisper my world
    [Ctrl+D]
    > ls
    fizz.py  fizz.rock

Using ``--exec``
~~~~~~~~~~~~~~~~

::

    > rockstar-py -i fizz.rock --exec
    1
    2
    Fizz!
    4
    Buzz!
    Fizz!
    7
    8
    Fizz!
    Buzz!
    11
    Fizz!
    13
    14
    FizzBuzz!
    16
    17
    Fizz!
    19
    Buzz!
    Fizz!
    22
    23
    Fizz!
    Buzz!
    26
    Fizz!
    28
    29
    FizzBuzz!
    31
    32
    Fizz!
    34
    Buzz!
    Fizz!
    37
    38
    Fizz!
    Buzz!
    41
    Fizz!
    43
    44
    FizzBuzz!
    46
    47
    Fizz!
    49
    Buzz!
    Fizz!
    52
    53
    Fizz!
    Buzz!
    56
    Fizz!
    58
    59
    FizzBuzz!
    61
    62
    Fizz!
    64
    Buzz!
    Fizz!
    67
    68
    Fizz!
    Buzz!
    71
    Fizz!
    73
    74
    FizzBuzz!
    76
    77
    Fizz!
    79
    Buzz!
    Fizz!
    82
    83
    Fizz!
    Buzz!
    86
    Fizz!
    88
    89
    FizzBuzz!
    91
    92
    Fizz!
    94
    Buzz!
    Fizz!
    97
    98
    Fizz!
    Buzz!

Contributing
------------

The project has basically reached its end, but I'm still accepting pull requests that improve speed and legibility of the
code.

Authors
-------

-  **yyyyyyyan** - *Initial work* - `yyyyyyyan`_

Contributors
------------

Huge thanks to everyone who is contribuing to this project. Check them out at `Contributors`_! 

License
-------

This project is licensed under the MIT License - see the `LICENSE`_ file
for details.

Acknowledgments
---------------

-  Hat tip to `dylanbeattie`_ for creating Rockstar
-  The FizzBuzz example works well. If valid code doesn’t work, create
   an issue so I can get a look.
-  I’ll work on the readibility and organization of the code, would love
   suggestions on how/where to do that.

.. _Rockstar: https://github.com/dylanbeattie/rockstar
.. _fizz.rock: https://github.com/yyyyyyyan/rockstar-py/blob/master/tests/fizz.rock
.. _yyyyyyyan: https://github.com/yyyyyyyan
.. _Contributors: https://github.com/yyyyyyyan/rockstar-py/graphs/contributors
.. _LICENSE: https://github.com/yyyyyyyan/rockstar-py/blob/master/LICENSE
.. _dylanbeattie: https://github.com/dylanbeattie/
