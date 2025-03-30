# Problema 7

#Implementa un programa que realice lo siguiente:

#Genere una lista de números aleatorios.
#Ordene la lista usando el algoritmo de Quicksort.
#Permita al usuario buscar un n´umero en la lista usando b´ usqueda binaria.
#El programa debe mostrar la lista antes y despu´ es del ordenamiento y los resul
#tados de la b´ usqueda.

import random

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
a = random.choice(lista)
b = random.choice(lista)
c = random.choice(lista)
d = random.choice(lista)
e = random.choice(lista)

listaaleatoria = print([a, b, c, d, e])

listaordenada = sorted(listaaleatoria)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

print(quicksort(lista))