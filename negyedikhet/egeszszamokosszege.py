
def main():
    egytol_szazig=sum(range(1, 101))
    print("Az 1-tol 100-ig számok összege:", egytol_szazig)
    egytol_szazig_szamjegyek="".join(str(i) for i in range(1, 101))
    szamjegyek= list(egytol_szazig_szamjegyek)
    szamjegyek_osszege=sum(int(i) for i in szamjegyek)
    print("Az 1-tol 100-ig számok számjegyeinek összege:", szamjegyek_osszege)

#############################################################################

if __name__ == "__main__":
    main()