from this import s


lista = [] #üres lista

# lista.append()
lista.append("Fifa")
lista.append("pubg")
lista.append("COD")
lista.append("Fortnite")
lista.append("GTA")

#kiiratas 3 féle képppen
#1.
print(lista)
print("*******************************************************")

#2.
for item in lista:
    print(item)
print("****************************************************")

#3.
#len függvény a lista hossza (hány elemet tartalmaz)
for i in range(len(s)):
    print(lista[i])

#szűrés    
for item in lista:
    if item == "COD":
        print("IGEN")
    else:
        print("NO")