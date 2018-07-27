rockstar-py
===========

Python transpiler for the esoteric language `Rockstar`_

Getting Started
---------------

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes.

Installing
~~~~~~~~~~

The easiest way is installing using pip:

::

   sudo pip install rockstar-py

You can also clone this project using git:

::

   git clone https://github.com/yanorestes/rockstar-py.git

Usage
-----

If you installed the package using pip, you can simply run rockstar-py in the command line:

::

   rockstar-py [--output OUTPUT.py] input.rock

You can also run the transpiler directly by ``rockstar.py``:

::

   python3 -W ignore -m rockstarpy [--output OUTPUT.py] input.rock

Contributing
------------

I’m accepting pull requests that improve speed and legibility of the
code.

Authors
-------

-  **Yan Orestes** - *Initial work* - `yanorestes`_

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
.. _yanorestes: https://github.com/yanorestes
.. _Contributors: https://github.com/yanorestes/rockstar-py/graphs/contributors
.. _LICENSE: https://github.com/yanorestes/rockstar-py/blob/master/LICENSE.txt
.. _dylanbeattie: https://github.com/dylanbeattie/