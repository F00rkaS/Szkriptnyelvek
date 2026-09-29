def main():
    eredeti =['auto', 'villamos', 'metro']
    nagybetus =[szo.upper() + "!" for szo in eredeti]
    print(nagybetus)
    nevek=['aladar', 'bela', 'cecil']
    nagybetusnev =[szo.upper()[:1] + szo[1:] for szo in nevek]
    print(nagybetusnev)
    nullak = [0 for i in range(10)]
    print(nullak)
    szamok = list(range(1,10))
    dupla= [i*2 for i in szamok]
    print(dupla)
    

if __name__  == "__main__":
    main()