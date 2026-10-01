import sys
import random as r

UPTO = 100


def main():
    for _ in range(UPTO):
        if _ % 10 == 0 and _ != 0:
            print()
        print(r.randint(0, 9), end="")


if __name__ == "__main__":
    main()