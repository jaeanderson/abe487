#!/usr/bin/env python3

import os
import sys

myargs = sys.argv[1:]	#assigns all input arguments into array

#if no input argument is given, then output usage statement and exit program with error message
if len(myargs) < 1:
        print('Usage: {} FILE [SEQUENCE] ARGS'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

seq_length = 5		#initialize default sequence length to 5 characters

#checks if two arguments given, is second input argument a digit, then assigns sequence length to given second argument
if len(myargs) > 1 and myargs[1].isdigit():
	seq_length=int(myargs[1])

fs_input = myargs[0]	#assigns first input argument to variable

#if valid input file, iterate file, output each sequence in file to specified sequence length; else output given input sequence to specified sequence length
if os.path.isfile(fs_input):
	for line in open(fs_input):
		print(line[0:seq_length])
else:
	print(fs_input[0:seq_length])
