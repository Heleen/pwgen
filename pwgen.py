#!/usr/bin/python

"""Password Generator
Generates a random password.

Requires:
    docopt
    xerox (optional)
    zxcvbn (optional)

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

If zxcvbn is installed the password strength will always be printed (crack time: "instant", "6 minutes" or "centuries", etc., score: [0,1,2,3,4] if crack time is less than [10**2, 10**4, 10**6, 10**8, Infinity]). See the Git repository of (python-)zxcvbn for more details.

For easy usage add the following to your .bashrc profile: alias pwgen='python [location to file]'.

TODO:
    * add regex option (for when you need a password which, for example, starts with a capital or has 3 numbers,...).

"""

import string
from itertools import repeat
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


class Password:

    # password_length
    # character_set

    def __init__(self, argv):

        """ Determine the length of the password """
        if argv['<length>']:
            self.password_length = int(argv['<length>'])
        else:
            self.password_length = password_length

        """ Determine the required characters for the password """
        self.character_set = []
        if not argv['--default']:
            if argv['--lowercase']:
                self.character_set += lowercase_letters
            if argv['--uppercase']:
                self.character_set += uppercase_letters
            if argv['--numbers']:
                self.character_set += numbers
            if argv['--characters']:
                self.character_set += characters
            elif argv['--charset']:
                self.character_set += list(argv['--charset'])

        if not self.character_set:
            self.character_set = default_character_set

    def generate(self):
        """ Generate the password """
        password = ''.join(  # Convert the list of characters to a string
            map(
                self.character_set.__getitem__,  # Map random indexes to their corresponding character from the character set
                [randint(0, len(self.character_set) - 1) for _ in repeat(None, self.password_length)]  # Generate list of random indexes
            )
        )
        return password


def main(argv={}):
    password = Password(argv).generate()

    """ Copy the password to clipboard? """
    if not argv['--no-clipboard']:
        try:
            import xerox
            xerox.copy(password)
        except ImportError:
            print no_xerox_error

    """ Print the password? """
    if argv['--print'] or argv['--no-clipboard']:
        print password

    """ Print password strength """
    try:
        from zxcvbn import password_strength
        strength = password_strength(password)
        print 'crack time: ' + strength['crack_time_display'] + ', score: ' + str(strength['score']) + ' out of 4'
    except ImportError:
        print no_zxcvbn_error


if __name__ == '__main__':
    main(docopt(__doc__, version='Password Generator 1.0'))
