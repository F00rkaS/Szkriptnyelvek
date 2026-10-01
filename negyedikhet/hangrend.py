mely=['a', 'á', 'o', 'ó', 'u', 'ú']
magas=['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']


def hangrend(word):
    melye=0
    magase=0
    for letter in word:
        if letter in mely:
            melye = 1
        elif letter in magas:
            magase = 1
    if melye + magase== 2:
        return "vegyes"
    elif melye==1:
        return "mely"
    elif magase==1:
        return "magas"
    else:
        return "semmilyen"


def main():
    
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
    hangrendek=[hangrend(word) for word in words]
    print(hangrendek)

if __name__ == "__main__":
    main()