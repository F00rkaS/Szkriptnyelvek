#!/usr/bin/env python3
hatvanyok = [0 if i == 0 else i**i for i in range(10)]

def munchausen(n):
    eredeti = n
    osszeg = 0
    while n > 0:
        szamjegy = n % 10
        osszeg += hatvanyok[szamjegy]
        
        if osszeg > eredeti:
            return False
        
        n //= 10
        
    return osszeg == eredeti

    
def main():
    for i in range(10000):
        if munchausen(i):
            print(i)
##############################################################################

if __name__ == "__main__":
    main()