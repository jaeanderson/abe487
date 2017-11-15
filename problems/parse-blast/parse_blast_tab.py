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

    print('\t'.join([r.get(x) for x in ['qseqid','sseqid','pident','evalue']]).rstrip())


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    pid_val = args.pct_id
    e_val = args.evalue
    blast_file = args.positional
    
    headers = 'qseqid sseqid pident length mismtch gapopen qstrt qend sstrt send evalue bitscore'.split()

    with open(blast_file, 'r') as bfile:
        reader = csv.reader(bfile, delimiter='\t')
        for i, line in enumerate(reader):
            row = dict(zip(headers, line))

            if pid_val != 0.0 or e_val is not None:
                if e_val is None and float(row['pident']) > pid_val:
                    output_parse(row)
                else:
                    if pid_val == 0.0 and float(row['evalue']) < e_val:
                        output_parse(row)
                    elif float(row['pident']) > pid_val and float(row['evalue']) < e_val:
                        output_parse(row)
            else:
                output_parse(row)

    bfile.close()
    

# --------------------------------------------------
if __name__ == '__main__':
    main()

