#!/usr/bin/env python3


def main():
    szam="1122"
    osszeg = 0
    hossz = len(szam)
    
    # Végigmegyünk a számsorozaton
    for i in range(hossz):
        aktualis_szam = int(szam[i])
        
        kovetkezo_index = (i + 1) % hossz
        kovetkezo_szam = int(szam[kovetkezo_index])
        

        if aktualis_szam == kovetkezo_szam:
            osszeg += aktualis_szam
            
    return osszeg

##############################################################################

if __name__ == "__main__":
    main()