Random Password Generator
=========================

Description
-----------

Generates a random password.

Requires
--------

* docopt
* xerox (optional)
* zxcvbn (optional)

Usage
-----

::

    pwgen.py [<length>] [-d | --default] [([-x | --clipboard] | [-p | --print])]
    pwgen.py [<length>] [-l | --lowercase] [-u | --uppercase] [-n | --numbers] [-c | --characters] [--charset=<chars>] [([-x | --clipboard] | [-p | --print])]
    pwgen.py ( -h | --help)

Options
-------

::

    -h --help           Show this screen.
    -d --default        Use default settings (14 -lunc).
    -l --lowercase      Add lowercase letters to the character set.
    -u --uppercase      Add uppercase letters to the character set.
    -n --numbers        Add numbers to the character set.
    -c --characters     Add default special characters to the character set.
    --charset=<chars>   Add other characters to the character set.
    -x --no-clipboard   Do not copy the password to clipboard, but print it to stdout instead.
    -p --print          Do print password to stdout and copy it to clipboard.

.. NOTE:: If zxcvbn is installed the password strength will always be printed (crack time: "instant", "6 minutes" or "centuries", etc., score: [0,1,2,3,4] if crack time is less than [10**2, 10**4, 10**6, 10**8, Infinity]). See `the Git repository of zxcvbn <https://github.com/rpearl/python-zxcvbn>`_ for more details.

.. NOTE:: For easy usage add the following to your .bashrc profile: ``alias pwgen='python [location to file]'``.

.. NOTE:: TODO: 

    * add regex option (for when you need a password which, for example, starts with a capital or has 3 numbers,...).
