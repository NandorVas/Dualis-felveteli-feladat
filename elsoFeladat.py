#abc--------------------------------------------------------------------------------------------------------------------
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

#function---------------------------------------------------------------------------------------------------------------
def keres(betu):
    i = 0
    while i < len(abc):
        if abc[i] == betu:
            return i
        i += 1
    return i

#bekérés----------------------------------------------------------------------------------------------------------------
uzenet = str(input("Írja be az üzenetet: "))
kulcs = str(input("Írja be a kulcsot: "))

#hibakeresés------------------------------------------------------------------------------------------------------------
if len(kulcs) < len(uzenet):
    print("HIBA!\nA kulcsnak minimum akkorának kell lennie, mint üzenetnek.")

#algoritmus-------------------------------------------------------------------------------------------------------------
uz = []
kul = []

for i in range(len(uzenet)):
    uz.append(keres(uzenet[i]))

for i in range(len(kulcs)):
    kul.append(keres(kulcs[i]))

megoldas = []

for i in range(len(uzenet)):
    if (uz[i]+kul[i]) < 27:
        megoldas.append(uz[i] + kul[i])
    else:
        megoldas.append((uz[i]+kul[i])%27)

rejtett = []

for i in range(len(uzenet)):
    rejtett.append(abc[megoldas[i]])

print(f"A rejtjelezett üzenet a következő: {''.join(rejtett)}")