#!/usr/bin/env python3
def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    result = ""
    for char in text:
        if char in chars:
            result += char
    return result

def main():
    print(valid("Barking!"))                              
    print(valid("KL754", chars="0123456789"))                   
    print(valid("BEAN", chars="abcdefghijklmnopqrstuvwxyz")) 

##############################################################################

if __name__ == "__main__":
    main()