#!/usr/bin/env python3

import os
import sys

myargs = sys.argv[1:]	#assigns all input arguments into array

#if no input argument is given, then output usage statement and exit program with error message
if len(myargs) != 1:
	print('Usage: {} FILENAME'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

file = myargs[0]	#assigns first input argument in variable

#checks if first input argument is a valid file, if not output statement and exit program with error message
if not os.path.isfile(file):
	print('"{}" is not a file'.format(file))
	sys.exit(1)
	
gc_counter = 0		#initialize gc counter to 0

#creates a list with each element assigned a line of the input file
temp=open(file,'r').read().split("\n")

#iterates over lines of file, count number of gc letters, output percentage of gc letters per line
for line in temp:
	#checks if end of list then exits iteration
	if line == '':
		break;

	#iterates characters per line and counts gc characters
	for char in enumerate(line):
		if char[1] in 'cCgG':
			gc_counter += 1

	#outputs integer percentage of gc characters per sequence 
	print("{}".format(int(gc_counter/len(line)*100)))

	gc_counter=0	#reinitialize gc counter after each line of file

