#!/usr/bin/env python3


import sys
import os
from collections import defaultdict

input_args=sys.argv[1:]			#assigns input arguments to list variable

#if input argument is not 1, then output usage message and exit program
if len(input_args) != 1:
	print('Usage: {} SEQ'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)


file='codons.rna'			#assigns file name to string variable

rna_dict = {}				#creates dictionary for rna codons and proteins

#opens and reads rna file and assigns codon as key and protein as value
with open(file, 'r') as f:
	for line in f:
		codon, protein = line.split()
		rna_dict[codon] = protein

sequence = sys.argv[1].upper()		#converts input argument to upper case and assigns to string variable
kmer_length = 3				#initialize length of kmers to length of 3


protein_translate = ''				#initialize string variable for codon to protein translation

#iterates sequence for given kmer_length and translate kmer matches to protein value  
for i in range(0, len(sequence), kmer_length):
	kmer = sequence[i:i+kmer_length]
	protein_translate += rna_dict[kmer]

#outputs translated protein
print(protein_translate)
