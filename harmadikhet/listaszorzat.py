def listaszorzat(lst):
    szorzat = 1
    for x in lst:
        szorzat *= x
    return szorzat

def main():
    lista = [1, 2, 3, 4, 5]
    print(listaszorzat(lista))


if __name__ == "__main__":
    main()