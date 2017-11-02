#!/usr/bin/env python3
"""FASTA Trimmer"""

import argparse
import os
import sys
from Bio import SeqIO
from Bio.Seq import Seq

# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(description='FASTA trimmer')
    parser.add_argument('positional', metavar='file', help='FASTA file')
    parser.add_argument('-s', '--start', help='Start position',
                        metavar='int', type=int, default=0)
    parser.add_argument('-e', '--end', help='End position',
                        metavar='int', type=int, default=0)
    parser.add_argument('-m', '--min', help='Minimum length',
                        metavar='int', type=int, default=0)
    parser.add_argument('-o', '--outfile', help='Output file',
                        metavar='str', type=str, default=None)
    return parser.parse_args()

# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    infile = args.positional			#name of input file
    start = args.start				#start position of sequence
    end = args.end				#end position of sequence
    min = args.min				#min length of sequence
    outfile = args.outfile			#name of output file

    #usage test for input arguments
    if not os.path.isfile(infile):
        print('--fasta "{}" is not valid'.format(infile))
        exit(1)   

    #opens output file as default value or given input argument filename
    if outfile is None:
         output_handle = open(os.path.basename(infile) + '.trimmed', 'wt')
    else:
         output_handle = open(outfile, 'wt')

    sequences = []				#initialize list for record_id and sequences
    
    #iterates over fasta file sequences and inputs into list based on input argument conditions
    for record in SeqIO.parse(infile, "fasta"):
        #if no start, end, or min arguments given
        if start == 0 and end == 0 and min == 0:
            sequences.append([record.id, str(record.seq)])
        #else if start argument is only given
        elif start != 0 and end == 0 and min == 0:
            sequences.append([record.id, str(record.seq[start - 1:])])
        #else if start and end arguments are given
        elif start != 0 and end != 0 and min == 0:
            sequences.append([record.id, str(record.seq[start - 1:end])])
        #else if start and min arguments are given
        elif start != 0 and min != 0 and end == 0 and (start + min) < len(record.seq):
            sequences.append([record.id, str(record.seq[start - 1:])])

    #outputs sequence_id and modified sequence to file
    for rec_id, seq in sequences:
        output_handle.write('>{}\n{} '.format(rec_id, seq))
    output_handle.close()

    #outputs number of sequences written to output file
    print('Wrote {} sequences to "{}"'.format(len(sequences), output_handle.name))

# --------------------------------------------------
if __name__ == '__main__':
    main()
