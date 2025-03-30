# Problema 8

#Implementa el algoritmo de Mergesort para ordenar una lista de n´ umeros in
#gresada por el usuario. El programa debe mostrar la lista antes y despu´ es del
#ordenamiento.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge_sort(left_half)  
        merge_sort(right_half) 

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
print("Lista original:", arr)
merge_sort(arr)
print("Lista ordenada:", arr)