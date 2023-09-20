# abc-------------------------------------------------------------------------------------------------------------------
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z", " "]

# function--------------------------------------------------------------------------------------------------------------
def keres(betu):
    i = 0
    while i < len(abc):
        if abc[i] == betu:
            return i
        i += 1
    return i

# beolvasás-------------------------------------------------------------------------------------------------------------
kulcsok = []

with open("words.txt", "r", encoding="UTF-8") as file:
    for sor in file:
        i = sor.strip()
        kulcsok.append(i)

# szavakKiválasztása----------------------------------------------------------------------------------------------------
elsoUz = input("Adja meg az első kódolt üzenetet: ")

masodikUz = input("Adja meg a második kódolt üzenetet: ")

# kulcs hossza----------------------------------------------------------------------------------------------------------
kulcs = []
rosszak = []

if len(elsoUz) > len(masodikUz):
    for i in range(len(elsoUz)):
        kulcs.append("")
else:
    for i in range(len(masodikUz)):
        kulcs.append("")

for i in range(len(kulcsok)):
    if len(kulcs) > len(kulcsok[i]):
        rosszak.append(kulcsok[i])

rosszak = set(rosszak)

rosszak = list(rosszak)

for i in range(len(rosszak)):
    kulcsok.remove(rosszak[i])

# a kulcs betűi---------------------------------------------------------------------------------------------------------
n = int(input("Adja meg hány darab szóra szűkítse a program a kulcsokat. (Ajánlott minél kevesebbet megadni. Pl.: 10.): "))

while len(kulcsok) >= n:
    betu = str(input("Adjon meg egy olyan betűt amire tesztelni szeretne: "))
    for i in range(len(elsoUz)):
        if elsoUz[i] == betu:
            kulcs[i] = betu
    for i in range(len(masodikUz)):
        if masodikUz[i] == betu:
            kulcs[i] = betu
    seg = ""
    rosszak = []
    indexek = []
    for i in range(len(kulcs)):
        if kulcs[i] == betu:
            indexek.append(i)
    for i in range(len(kulcsok)):
        for j in range(len(indexek)):
            if kulcsok[i][indexek[j]] != betu:
                rosszak.append(kulcsok[i])
    rosszak = set(rosszak)
    rosszak = list(rosszak)
    for i in range(len(rosszak)):
        kulcsok.remove(rosszak[i])
    print(f'Szűkítette a kulcsok számát. A mardék szavak száma: {len(kulcsok)}')


if n == 0:
    print("Sajnáljuk, nincs egyező kulcs.")
else:
    print(f'A szűkítés véget ért. A szűkített szavai listája egy kulcsok.txt file-ban található.')
    with open("kulcsok.txt", "w", encoding="UTF-8")as file:
        for i in range(len(kulcsok)):
            file.write(str(kulcsok[i]))
