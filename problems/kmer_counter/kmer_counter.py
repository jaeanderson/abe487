#!/usr/bin/env python3


import sys
import os
from collections import Counter

input_args=sys.argv[1:]		#assigns input arguments into array

#checks if two input arguments are given else prints error message and exits program
if len(input_args) <=1 or len(input_args) >= 3:
	print('Usage: {} LEN STR'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

arg1 = input_args[0]		#assigns kmer length argument as string variable

#if kmer length argument is 0 or not a digit then print error message and exit program
if arg1.isdigit():
	if arg1 == '0':
		print('Kmer size "{}" must be > 0'.format(arg1))
		sys.exit(1)
else:
	print('Kmer size "{}" is not a number'.format(arg1))
	sys.exit(1)

kmer_length = int(arg1)		#assigns kmer length argument as integer variable
sequence = input_args[1]	#assigns sequence argument as string variable

#if kmer length argument is greater than length of sequence argument, then output error message and exit program
if len(sequence) < kmer_length:
	print('There are no {}-mers in "{}"'.format(kmer_length,sequence))
	sys.exit(1)

#calculates total number of kmers within given sequence and kmer length
num_kmers = len(sequence) - kmer_length + 1
	
#counts number of kmers based on kmer length for given sequence
kmer_count=Counter([sequence[i:i+kmer_length] for i in range(0, num_kmers, 1)])

#output given sequence and sorted kmers with repeated value
print(sequence)
for base, k_count in sorted(kmer_count.items()):
	print('{} {}'.format(base, k_count))

