#!/usr/bin/env python3


def main():
    szamok=[i for i in range(1000) if i % 5 == 0 and i % 3 == 0]
    print(sum(szamok))

##############################################################################

if __name__ == "__main__":
    main()