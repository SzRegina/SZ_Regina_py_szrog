"""Programozás alapismeretek összefoglaló
A feladatokat egyazon fájlban, lépésenként kell megcsinálni!
1.	Kérjünk be 1 bármilyen számot
2.	A szám legyen [5; 30] intervallumban, ha nem jó, akkor: „hiba!”
3.	Kérjünk be egy számot [5; 30], amíg nem jó, addig újra kérjük be
4.	Kérjünk be egy keresztnevet
5.	Kérjünk be szóközzel egy teljes nevet és 
csak a vezetéknevet írjuk ki
6.	Kérjünk be -amíg nem jó- egy minimum hárombetűs szót
7.	Írjuk ki, hogy egyezik e az első és az utolsó betű
8.	Írjuk ki, hogy egyezik e a második és az utolsó betű
9.	Mondjuk meg, hogy nagybetű e az első betű
10.	Generáljunk egy véletlen számot
11.	Legyen [-5; 15] intervallumban
12.	Generáljunk és jelenítsünk meg 5 db számot a fenti intervallumból
13.	A megjelenítést vesszővel elválasztva végezzük, a végén nincs vessző
14.	Rakjuk egy listába a 3, -5, 7 értékeket
15.	Jelenítsük meg a lista elemeit az alábbi formában 
(az a. b. c. is generálva legyen, ne másik tömbben): 
a.	1. elem: 3
b.	2. elem: -5
c.	3. elem: 7
16.	Generáljunk 5 db véletlenszámot [5; 15] intervallumban, 
egy listába rakva jelenítsük meg őket
17.	A 3. feladat bekért számát osszuk el a generált lista utolsó elemével,
írjuk ki 2 tizedes pontossággal az eredményt
18.	A 14. feladat 1. elemét(3) osszuk el a generált lista (16. feladat) középső elemével,
írjuk ki 4 tizedes pontossággal az eredményt
19.	Mennyi a generált lista (16. feladat) elemeinek összege?
20.	Mennyi a generált lista (16. feladat) elemeinek átlaga?
21.	Hány darab hárommal osztható szám van benne?
22.	Melyik helyen van a legnagyobb és a legkisebb szám?
23.	Van benne 13? Ha megvan a válasz, akkor álljon le a vizsgálat!
24.	Minden elem nagyobb 10? Amint kiderül, hogy nem, álljon le a vizsgálat!
25.	Van benne / hány darab tökéletes számot tartalmaz a lista?
26.	Van benne / hány darab prímszámot tartalmaz a lista?
A feladatok készüljenek el metódusokba szervezve is, 
a meglévőt kell kiszervezni eljárásokba! 
A metódusoknak ne legyen paramétere, a több eljárásban is használt
változókat szervezzük ki az osztály szintjén elérhetőre!
Az utolsó kettő feladatot függvényekkel oldjuk meg!"""

#1.
akarmilyen = input("Kérlek, adj meg egy számot! ")
#2-3.
def akarmi():
    akarmilyen2 = int(input("Kérlek adj meg egy számot 5 és 30 között! "))
    while akarmilyen2 < 5 or 30 < akarmilyen2:
        akarmilyen2 = int(input("Hiba! Kérlek adj meg egy számot 5 és 30 között! "))
    else:
        print(f"A beírt számod a/az {akarmilyen2}!")
        return akarmilyen2


#4. Keresztnév
def nev():
    k_nev = str(input("Kérlek, adj meg egy keresztnevet! "))
#5. Teljes[szóköz]név - de csak a vezetéknevet!
def telnev():
    vnev = str(input("Add meg a vezetékneved! "))
    knev = str(input("Add meg a keresztneved! "))
    print(vnev + " " + knev)
    print(str(vnev))
#6. while 3 betűs szó!
def harombetu():
    szo = input("Kérlek, adj meg egy minimum 3 betűs szót! ")
    while len(szo) < 3:
        szo = input("Hiba! Kérlek, adj meg egy minimum 3 betűs szót! ")
    else:
        print("Köszi, ez egy jó szó!")
#7. Egyezik-e az 1. és utolsó betű!
def el_ut():
    random_szo = input(str("Adj meg egy tetszőleges szót! Megnézem, ugyanaz-e az első és az utolsó betűje! "))
    if random_szo[0] == random_szo[len(random_szo)-1]:
        print("Yep, same.")
    else:
        print("Nem ugyanaz az eleje, mint a vége! ")
#8.Ua. csak 2. és utolsó betűvel:
def ma_ut():
    masik_szo = input(str("Kérlek, adj meg egy másik szót, a 2. és utolsó betűjét fogom megvizsgálni! "))
    if masik_szo[1] == masik_szo[len(masik_szo)-1]:
        print("A 2.és utolsó betű ua.!")
    else:
        print("Nem, nem ua. a kettő.")
#9. Nagybetű-e?
def nagybetu_e():
    szoo = input("Légyszi, még egy szót! ")
    if szoo[0] == szoo[0].upper():
        print("A megadott szó első betűje nagybetű!")
    else:
        print("Nem, nem nagybetűs!")

#10.-11.

import random

def randomos():
    print(random.randrange(-5, 16))
#12.-13. 5 db. [-5, 15] közöttből


def randomos2():
    randomlist = random.sample(range(-15, 31), 5)
    print(randomlist)
"""a lényeg:
syntax:
random.sample(sequence/a lista, k)
    sequence/lista: amiből dolgozzon
        itt ugye hozzá lett csapva egy [-15, 30]-as intervallum
    k: vagy egy szám vagy k= valami szám
        ahány darabot ki kell vennie a listából !!!!!
"""
#14.-15 listában a 3, -5, 7 értékek és legyen hozzájuk rendelve a,b, c
def tizennegy_ot():
    lista = [3, -5, 7]
    lista2 =["a", "b", "c"]
    print(f"{lista2[0]}. 1. elem: {lista[0]}\n{lista2[1]}. 2. elem: {lista[1]}\n{lista2[2]}. 3. eleme: {lista[0]}")

#16.-17. [5-15] * 5 random szám
akarmi2 = int(input("Kérlek, adj meg egy számot! "))
def random_ot():
    random_lista = random.sample(range(5, 15), 5)
    print(random_lista)
    tizenhetes = akarmi2 / (random_lista[-1])
    print("{0:.2f}".format(tizenhetes))

#18.






