#!/usr/bin/env python3

import os
import sys

myargs = sys.argv[1:]	#assigns input arguments into array

#if no input argument is given, then print usage statement and exit program with error message
if len(myargs) != 1:
	print('Usage: {} SEQUENCE'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

sequence = myargs[0]	#initialize sequence to first input argument
gc_counter = 0		#initialize gc counter to 0

#iterates input sequence counting number of gc letters
for letter in sequence:
	if letter in 'cCgG':
		gc_counter += 1

#output percentage of gc letters in input sequence
print("{0:.0%}".format(gc_counter/len(sequence)) + " GC")
 
