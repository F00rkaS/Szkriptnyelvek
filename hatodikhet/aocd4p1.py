def is_valid_passphrase(passphrase):

    words = passphrase.split()
    
    # Ha a szavakból képzett halmaz hossza megegyezik az eredeti lista hosszával,
    # az azt jelenti, hogy nem volt ismétlődő elem, amit a set() eldobott volna.
    return len(words) == len(set(words))

def main():

    print("Példák")
    print(f"'aa bb cc dd ee' érvényes? -> {is_valid_passphrase('aa bb cc dd ee')}")     # Várható: True
    print(f"'aa bb cc dd aa' érvényes? -> {is_valid_passphrase('aa bb cc dd aa')}")     # Várható: False
    print(f"'aa bb cc dd aaa' érvényes? -> {is_valid_passphrase('aa bb cc dd aaa')}")   # Várható: True
    
    
    valid_count = 0
    try:
        with open('input.txt', 'r') as file:
            for line in file:
                if is_valid_passphrase(line.strip()):
                    valid_count += 1
        print(f"\nAz érvényes jelmondatok száma az adatbázisban: {valid_count}")
    except FileNotFoundError:
        print("\nNem található 'input.txt' nevű fájl.")
    

if __name__ == '__main__':
    main()