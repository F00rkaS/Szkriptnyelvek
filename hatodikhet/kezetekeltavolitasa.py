#!/usr/bin/env python3

def remove_accents_basic(text):

    ekezetes = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
    mentes   = "aeiooouuuAEIOOOUUU"
    
    for i in range(len(ekezetes)):
        text = text.replace(ekezetes[i], mentes[i])
        
    return text

def remove_accents_dict(text):
    accent_dict = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ö': 'o', 'ő': 'o', 'ú': 'u', 'ü': 'u', 'ű': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ö': 'O', 'Ő': 'O', 'Ú': 'U', 'Ü': 'U', 'Ű': 'U'
    }
    
    eredmeny = ""
    for char in text:
        eredmeny += accent_dict.get(char, char)
        
    return eredmeny

def main():
    teszt_szoveg = "A katalán zászló, a Senyera színeit fogja viselni a következő idény során..."
    
    print("1. Megoldás (replace)")
    print(remove_accents_basic(teszt_szoveg))
    
    print("\n2. Megoldás (dictionary)")
    print(remove_accents_dict(teszt_szoveg))

    
if __name__ == '__main__':
    main()