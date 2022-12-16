import random


lista = []

#feltöltjüka listát random számokkal
for i in range(10): #10 db szám lesz a listákkal
    lista.append(random.randint(1,100))
# print(lint)

#feladat
# Irjuk ki a 10 nel nagyobb számokat
for i in range(len(lista)):
    if lista[i] >= 10:
        print(lista[i])    
    