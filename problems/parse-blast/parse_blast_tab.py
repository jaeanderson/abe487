#!/usr/bin/env python3
"""Parse-Blast-er"""

import argparse
import sys
import csv

# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(description='Parse BLAST tab')
    parser.add_argument('positional', metavar='file', help='BLAST tab output')
    parser.add_argument('-p', '--pct_id', help='Percent identity',
                        metavar='float', type=float, default=0.0)
    parser.add_argument('-e', '--evalue', help='Maximum value',
                        metavar='float', type=float, default=None)
    return parser.parse_args()

# --------------------------------------------------
def output_parse(r):
    """print dictionary row with tabs"""

    print('\t'.join([r.get(x) for x in ['qseqid','sseqid','pident','evalue']]))

# --------------------------------------------------
def main():
    """main"""

    #input arguments
    args = get_args()
    pid_val = args.pct_id
    e_val = args.evalue
    blast_file = args.positional

    #blastn outfmt-6 headers    
    headers = 'qseqid sseqid pident length mismtch gapopen qstrt qend sstrt send evalue bitscore'.split()

    #opens and reads tab delimited input file
    with open(blast_file, 'r') as bfile:
        reader = csv.reader(bfile, delimiter='\t')

        #creates dictionary for each row in file with headers
        for line in reader:
            row = dict(zip(headers, line))

            #parses dictionary according to input arguments
            if pid_val != 0.0 or e_val is not None:
                if e_val is None and float(row['pident']) >= pid_val:
                    output_parse(row)
                else:
                    if pid_val == 0.0 and float(row['evalue']) <= e_val:
                        output_parse(row)
                    elif float(row['pident']) >= pid_val and float(row['evalue']) <= e_val:
                        output_parse(row)
            else:
                output_parse(row)

    #closes input file
    bfile.close()
    

# --------------------------------------------------
if __name__ == '__main__':
    main()

