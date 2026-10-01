def main():
    negyzetekosszeg = sum(i**2 for i in range(1, 101))
    osszegeknyegszetet = sum(i for i in range(1, 101)) ** 2
    kulonbseg = osszegeknyegszetet - negyzetekosszeg
    print(kulonbseg)


if __name__ == "__main__":
    main()