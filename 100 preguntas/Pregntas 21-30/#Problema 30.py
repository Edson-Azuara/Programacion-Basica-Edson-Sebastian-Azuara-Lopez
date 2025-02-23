# Problema 30

def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso
print(suma_lista([1, 2, 3, 4, 5]))