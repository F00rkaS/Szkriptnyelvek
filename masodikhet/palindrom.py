def palindrom(s):
    s = s.lower()
    return s == s[::-1]


def main():
    
    print(palindrom("görögg"))


if __name__ == "__main__":
    main()