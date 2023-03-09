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
osszeg=0
for het in hianyzasok:
   osszeg+=sum(het)

print(f"1. feladat: {osszeg} óra hiányzás volt összesen")


# 2. Volt-e olyan hét, amikor nem volt hiányzó?
index=0
while index<len(hianyzasok) and not(sum(hianyzasok[index])==0):
    index+=1
van=index<len(hianyzasok)
if van:
    print(f"2. feladat: Volt olyan hét, amikor nem volt hiányzó. ")
else:
    print(f"2. feladat: Nem volt olyan hét, amikor nem volt hiányzó. ")


# 3. Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt
index=0
while index<len(hianyzasok) and not(sum(hianyzasok[index])<5):
    index+=1
if index<len(hianyzasok): 
    print(f"3. feladat: Volt olyan hét, amikor ötnél kevesebb hiányzó volt")
else:
    print(f"3. feladat: Nem volt olyan hét, amikor ötnél kevesebb hiányzó volt ")


# 4. Melyik héten volt a legtöbb hiányzás?
max_index=0
for index in range(len(hianyzasok)):
    if sum(hianyzasok[index])>sum(hianyzasok[max_index]):
        max_index=index

print(f"4. feladat: A legtöbb hiányzás a {max_index+1} héten volt {sum(hianyzasok[max_index])}")

# 5. Hányadik héten volt egyetlen hiányzás?
#5. feladat: 4. héten volt egyetlen hiányzás
index=0
while index<len(hianyzasok) and not(sum(hianyzasok[index])==1):
    index+=1

van=index<len(hianyzasok)
if van:
    sorszam=index
    print(f"5. feladat: {sorszam+1} héten volt egyetlen hiányzás")
else:
    sorszam=-1
    print(f"5. feladat: Egyik héten sem volt egyetlen hiányzás")
