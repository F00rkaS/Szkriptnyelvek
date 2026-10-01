def main():
    magassag = int(input("Add meg a magasságot: "))
    if magassag%2 ==0: 
        print("A magasság nem lehetpáros")
        return
    uresek=magassag//2
    for i in range(uresek):
        print(" "*(uresek-i), end="")
        print("*"*(2*i+1))
    for i in range(uresek-1, -1, -1):
        print(" "*(uresek-i), end="")
        print("*"*(2*i+1))

    





if __name__ == "__main__":
    main()