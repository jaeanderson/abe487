#!/usr/bin/env python3
"""count the vowels in a word"""

import os
import sys

myarg = sys.argv[1:]

if len(myarg) < 1:
        script = os.path.basename(sys.argv[0])
        print('Usage: {} STRING'.format(script))
        sys.exit(1)

word=myarg[0]
vowel_ctr=0
vowels='aeiou'
for letter in word:
	if letter in vowels:
		vowel_ctr += 1

if vowel_ctr == 1:
	print('There is', vowel_ctr, 'vowel in', '"' + word + '."')
else:
	print('There are', vowel_ctr, 'vowels in', '"' +  word + '."')

