def main():
#1.feladat
    eredeti =['auto', 'villamos', 'metro']
    nagybetus =[szo.upper() + "!" for szo in eredeti]
    print(nagybetus)

#3.feladat
    nevek=['aladar', 'bela', 'cecil']
    nagybetusnev =[szo.upper()[:1] + szo[1:] for szo in nevek]
    print(nagybetusnev)

#3.feladat
    nullak = [0 for i in range(10)]
    print(nullak)

#4.feladat
    szamok = list(range(1,10))
    dupla= [i*2 for i in szamok]
    print(dupla)

#5.feladat
    stringszamok= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    szamoksztringbol= [int(i) for i in stringszamok]
    print(szamoksztringbol)

#6.feladat
    egyszamsztringkent="1234567"
    szamokegyszamsztringbol= [int(i) for i in egyszamsztringkent]
    print(szamokegyszamsztringbol)


#7.feladat
    mondat='The quick brown fox jumps over the lazy dog'
    szavakhosszaamondatbol= [len(szo) for szo in mondat.split()]
    print(szavakhosszaamondatbol)

#8.feladat
    maondat2="python is an awesome language"
    mondatkezdobetui= [szo[0] for szo in maondat2.split()]
    print(mondatkezdobetui)

#9.feladat
    mondat3='The quick brown fox jumps over the lazy dog'
    szoeshosszak= [(szo, len(szo)) for szo in mondat3.split()]
    print(szoeshosszak)

#10.feladat
    tiznelkissebparos= [i for i in range(10) if  i % 2 == 0]
    print(tiznelkissebparos)

#11.feladat
    maceras=[i*i for i in range(20) if i % 2 == 0]
    print(maceras)

#12.feladat
    macerasabb=[i*i for i in range(20) if i % 2 == 0 and i*i % 10 == 4]
    print(macerasabb)

#13.feladat
    abc=[]

#14.feladat
    rosszszavak=[' apple ', ' banana ', ' kiwi']
    joszavak=[szo.strip() for szo in rosszszavak]
    print(joszavak)

#15.feladat
    bitek=[1, 0, 1, 1, 0, 1, 0, 0]
    bitekstring=[str(b) for b in bitek]
    print(bitekstring)


if __name__  == "__main__":
    main()