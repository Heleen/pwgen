Random Password Generator
=========================

Description
-----------

Generates a random password.

Requires
--------

* docopt
* xerox (optional)

Usage
-----

pygen.py [<length>] [-d | --default] [([-x | --clipboard] | [-p | --print])]
pygen.py [<length>] [-l | --lowercase] [-u | --uppercase] [-n | --numbers] [-c | --characters] [--charset=<chars>] [([-x | --clipboard] | [-p | --print])]
pygen.py ( -h | --help)

Options
-------

-h --help           Show this screen.
-d --default        Use default settings (14 -lunc).
-l --lowercase      Add lowercase letters to the character set.
-u --uppercase      Add uppercase letters to the character set.
-n --numbers        Add numbers to the character set.
-c --characters     Add default special characters to the character set.
--charset=<chars>   Add other characters to the character set.
-x --no-clipboard   Do not copy the password to clipboard, but print it to stdout instead.
-p --print          Do print password to stdout and copy it to clipboard.

.. NOTE:: For easy usage add the following to your .bashrc profile: alias pwgen='python [location to file]'

.. TODO:: Add password strength checker.
