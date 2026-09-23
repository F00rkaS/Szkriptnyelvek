def palindrom_iterativ(aszo):
    bal = 0
    jobb = len(aszo) - 1
    while bal < jobb:
        if aszo[bal] != aszo[jobb]:
            return False
        bal += 1
        jobb -= 1
    return True


def palindrom_rekurziv(aszo, bal, jobb):
    if bal >= jobb:
        return True
    if aszo[bal] != aszo[jobb]:
        return False
    return palindrom_rekurziv(aszo, bal + 1, jobb - 1)


def main():
    aszo ="görög"

    #(2) Iteratív módszer. A sztringről nem készíthetünk másolatot.
    print(palindrom_iterativ(aszo))
    #(3) Rekurzív módszer. Csak hogy szokjuk a rekurziót is.
    print(palindrom_rekurziv(aszo, 0, len(aszo) - 1))

if __name__ == "__main__":
    main()