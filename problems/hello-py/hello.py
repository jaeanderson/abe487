#!/usr/bin/env python3
"""say hello to the arguments"""

import os
import sys

myarg = sys.argv[0]
names = sys.argv[1:]

if len(names) < 1:
	script = os.path.basename(myarg)
	print('Usage: {} NAME [NAME2...]'.format(script))
	sys.exit(1)

num_people = len(names)

if num_people == 1:
	print('Hello to the', num_people, 'of you: {}!'.format(*names))
elif num_people == 2:
	print('Hello to the', num_people, 'of you: {}!'.format(' and '.join(names)))
else:
	lastname = names.pop(-1)
	print('Hello to the', num_people, 'of you: {}'.format(', '.join(names)) + ', and',lastname + '!')


