#!/usr/bin/env python3
"""Hamming"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(description='Hamming')
    parser.add_argument('positional1', metavar='str1', help='A positional argument 1')
    parser.add_argument('positional2', metavar='str2', help='A positional argument 2')
    return parser.parse_args()
# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    s1 = args.positional1
    s2 = args.positional2

    #initialize hamming and string difference
    ham_ctr = 0
    diff = 0

    #finds minimum length between two strings
    min_len = min(len(s1), len(s2))
    
    #determines difference between two unequal strings
    if len(s1) != len(s2):
        max_len = max(len(s1), len(s2))
        diff = max_len - min_len

    #assuming two strings are of equal length
    #counts number of differing characters up to minimum length string
    for char in range(0, min_len):
        if s1[char] is not s2[char]:
            ham_ctr +=1

    #outputs hamming distance
    print(ham_ctr + diff)
        
# --------------------------------------------------
if __name__ == '__main__':
    main()
