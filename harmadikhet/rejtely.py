TEXT="""
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

def megoldas(TEXT, eltolas):
    helyreallitott = ""
    for c in TEXT:
        if c.isalpha():
            if c.islower():
                helyreallitott += chr((ord(c) - ord('a') + eltolas) % 26 + ord('a'))    #betu indexe - kis a indexe, igy tudjuk miaz index. ehez jon az eltolas, majd modulo 26 hogy korbe forogjon az abc es ne menjen el rosz helyekre az inex
            else:
                helyreallitott += chr((ord(c) - ord('A') + eltolas) % 26 + ord('A'))
        else:
            helyreallitott += c
    return helyreallitott

def main():
    eltolas=ord("O")-ord("Q")
    print(megoldas(TEXT, eltolas))

if __name__ == "__main__":
    main()