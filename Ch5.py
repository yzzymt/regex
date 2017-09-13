# -*- coding: UTF-8 -*-
import re

re.search(r'\b[1][24680]\b', ' 12 ')
'''By default Unicode alphanumerics are the ones used,
but this can be changed by using the ASCII flag.
Inside a character range, \b represents the backspace character,
for compatibility with Python’s string literals.'''

re.search(r'\b[1][24680[^2]]\b', '14')
