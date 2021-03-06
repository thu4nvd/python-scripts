#!/usr/bin/python3

import re

text = '''
42
1,234
6,368,745
3212,34,567
12.110
1234
1,234,567,789
'''

mo = re.compile(r'''
    ^
    \d{1,3}(?:,\d{3})*
    $
    ''', re.VERBOSE | re.MULTILINE)

print(mo.findall(text))
