#0. feladat: A hianyzasok.txt beolvasása listákba

hianyzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="utf-8") as fm:
    for sor in fm:
        seged_lista=sor.strip().split(",")
        # l=[]
        # for szam in seged_lista:
        #     l.append(int(szam))
        # hianyzasok.append(l)
        hianyzasok.append(list(map(int, seged_lista)))

# 1. Hány óra hiányzás volt összesen?
#1. feladat: 30 óra hiányzás volt összesen

osszeg=0
for het in hianyzasok:
   osszeg+=sum(het)

print(f"1. feladat: {osszeg} óra hiányzás volt összesen")


# 2. Volt-e olyan hét, amikor nem volt hiányzó?
# 2. feladat: Nem volt olyan hét, amikor nem volt hiányzó

print("2. feladat: Nem volt olyan hét, amikor nem volt hiányzó")