#Pregunta 17

#Pila
pila = list()

def insertarPila(pila, elemento):
    pila.append(elemento)
    return pila

def eliminarPila(pila):
    elementoFinal = pila[len(pila)-1]
    pila.remove(elementoFinal)
    return pila

if __name__ == "__main__":
    estupila = list()
    insertarPila(estupila,1)
    print(estupila)
    insertarPila(estupila,"mi pelo")
    print(estupila)
    insertarPila(estupila,"ideota")
    print(estupila)
    eliminarPila(estupila)
    print(estupila)

#Cola

def cuadrado(numero):
    return numero ** 2 
# Retorna el cuadrado

resultado = cuadrado(4)
print("El cuadrado de 4 es:", resultado)


#Lista enlazada

from random import randint

listaP = list()
listaN = list()
elementos = int(input("Introduce la cantidad de elementos: "))

for cont in range(-elementos, elementos):
    if cont < 0:
        listaN.append(randint(-100,0))
    elif cont > 0:
        listaP.append(randint(1,100))
    else:
        listaP.append(randint(0,1))
        
listaCompleta = listaN + listaP

print(listaCompleta)

listaN.extend(listaP)

print(listaN)


num = int(input("Introduce un número a buscar: "))

for itm in listaCompleta:
    if itm == num:
        print("El numero se encontraba en la posición ", listaCompleta.index(itm))
        break
