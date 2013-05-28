#!/usr/bin/python

"""Password Generator
Generates a random password.

Requires:
    docopt
    xerox (optional)

Usage:
    pwgen.py [<length>] [-d | --default] [([-x | --clipboard] | [-p | --print])]
    pwgen.py [<length>] [-l | --lowercase] [-u | --uppercase] [-n | --numbers] [-c | --characters] [--charset=<chars>] [([-x | --clipboard] | [-p | --print])]
    pwgen.py ( -h | --help)

Options:
    -h --help           Show this screen.
    -d --default        Use default settings (14 -lunc).
    -l --lowercase      Add lowercase letters to the character set.
    -u --uppercase      Add uppercase letters to the character set.
    -n --numbers        Add numbers to the character set.
    -c --characters     Add default special characters to the character set.
    --charset=<chars>   Add other characters to the character set.
    -x --no-clipboard   Do not copy the password to clipboard, but print it to stdout instead.
    -p --print          Do print password to stdout and copy it to clipboard.

For easy usage add the following to your .bashrc profile: alias pwgen='python [location to file]'

TODO:
    * add password strength checker;
    * add regex option (for when you need a password which, for example, starts with a capital or has 3 numbers,...).

"""

import string
from docopt import docopt
from random import randint

""" Global error definitions """
no_xerox_error = "Password not copied to clipboard, please install Xerox: https://github.com/kennethreitz/xerox."
no_zxcvbn_error = "The strength of the password could not be estimated, please install zxcvbn: https://pypi.python.org/pypi/zxcvbn/1.0."

""" Global variables """
lowercase_letters = list(string.lowercase[:26])
uppercase_letters = list(string.uppercase[:26])
numbers = map(str, range(0, 9))
characters = list("!@#$%^&*(){}][=/+?\-|_;:,.<>")
default_character_set = lowercase_letters + uppercase_letters + numbers + characters
password_length = 14  # Default password length, can be overwritten with positional argument


def main(argv={}):
    global password_length

    """ Determine the length of the password """
    if argv['<length>']:
        password_length = int(argv['<length>'])

    """ Determine the required characters for the password """
    character_set = []
    if not argv['--default']:
        if argv['--lowercase']:
            character_set += lowercase_letters
        if argv['--uppercase']:
            character_set += uppercase_letters
        if argv['--numbers']:
            character_set += numbers
        if argv['--characters']:
            character_set += characters
        elif argv['--charset']:
            character_set += list(argv['--charset'])

    if not character_set:
        character_set = default_character_set

    """ Generate the password """
    password = ''.join(  # Convert the list of characters to a string
        map(
            character_set.__getitem__,  # Map random indexes to their corresponding character from the character set
            [randint(0, len(character_set) - 1) for x in xrange(password_length)]  # Generate list of random indexes
        )
    )

    """ Copy the password to clipboard and/or print the password """
    if not argv['--no-clipboard']:
        try:
            import xerox
            xerox.copy(password)
        except ImportError:
            print no_xerox_error
    if argv['--print'] or argv['--no-clipboard']:
        print password
    try:
        from zxcvbn import password_strength
        strength = password_strength(password)
        print strength['crack_time_display'], strength['score']
    except ImportError:
        print no_zxcvbn_error


if __name__ == '__main__':
    main(docopt(__doc__, version='Password Generator 1.0'))
