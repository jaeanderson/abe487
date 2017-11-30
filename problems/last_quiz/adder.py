#!/usr/bin/env python3

"""docstring"""

import argparse
import sys
# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(description='Argparse Python script')
    parser.add_argument('positional1', metavar='arg1', help='A positional argument', default=None)
    parser.add_argument('positional2', metavar='arg2', help='A positional argument', default=None)

    return parser.parse_args()

    
# --------------------------------------------------
def main():
    """main"""
    args = get_args()

    pos_arg1 = args.positional1
    pos_arg2 = args.positional2

    print('positional1 = "{}"'.format(pos_arg1))
    print('positional1 = "{}"'.format(pos_arg2))

    if isinstance(pos_arg1, int) and isinstance(pos_arg2, int):
        print(int(pos_arg1) + int(pos_arg2))

    

    print(type(pos_arg1))
    print(type(pos_arg2))
    print(isinstance(pos_arg1, int))    


# --------------------------------------------------
if __name__ == '__main__':
    main()

print('OK')
