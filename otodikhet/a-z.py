#!/usr/bin/env python3

import os
import sys


def main():
    program_name = os.path.basename(sys.argv[0])
    abc="abcdefghijklmnopqrstuvwxyz"

    
    if program_name.startswith('z'):
        abc = abc[::-1]

    print(abc)

##############################################################################

if __name__ == "__main__":
    main()