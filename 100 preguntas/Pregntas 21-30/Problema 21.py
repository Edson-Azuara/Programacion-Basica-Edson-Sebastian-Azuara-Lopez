# Problema 21

#lista aleatoria

from random import randint 
x = randint(1,100)

print(x)

listaP = list()
ListaN = list()

elementos = int(input("introduce cantidad elementos"))

for cont in range(0, elementos):
    if cont<0:
        ListaN.append(randint(1,100))
    elif cont>0:
        listaP.appennd(randint(1,100))
    else:
        listaP.append(randint(0,1))

Listacompleta = ListaN + listaP

print(Listacompleta)

listaP.extend(ListaN)

print(listaP)
