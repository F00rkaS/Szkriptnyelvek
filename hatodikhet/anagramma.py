def normalize(s):
    return s.lower().replace(" ", "")

def is_anagram_trivial(s1, s2):
    """
    Triviális módszer: A normalizált sztringek karaktereit sorba rendezzük.
    Ha a két rendezett lista megegyezik, akkor a két szó anagramma.
    """
    return sorted(normalize(s1)) == sorted(normalize(s2))

def is_anagram_nontrivial(s1, s2):
    """
    Nemtriviális módszer: Szótár (dictionary) segítségével megszámoljuk a karaktereket.
    Ez a módszer hatékonyabb (O(n) időbonyolultságú), mint a sorba rendezés.
    """
    norm1 = normalize(s1)
    norm2 = normalize(s2)
    
    # Ha a hosszuk nem egyezik, biztosan nem anagrammák
    if len(norm1) != len(norm2):
        return False
        
    char_counts = {}
    
    # Megszámoljuk az első sztring karaktereit
    for char in norm1:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Csökkentjük a számlálót a második sztring karakterei alapján
    for char in norm2:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1
        
    return True

def main():
   
    print("--- Angol példák ---")
    print(is_anagram_trivial("listen", "silent"))                  # True
    print(is_anagram_nontrivial("A gentleman", "Elegant man"))     # True
    print(is_anagram_trivial("Clint Eastwood", "Old west action")) # True
    print(is_anagram_nontrivial("dormitory", "dirty room"))        # True
    
    print("\n--- Magyar példák ---")
    print(is_anagram_trivial("étel", "élet"))                      # True
    print(is_anagram_nontrivial("papi", "pipa"))                   # True
    print(is_anagram_trivial("kolostor", "rostokol"))              # True
    
    # Egy hamis eset tesztelése
    print("\n--- Hamis eset tesztje ---")
    print(is_anagram_nontrivial("alma", "korte"))                  # False

if __name__ == '__main__':
    main()