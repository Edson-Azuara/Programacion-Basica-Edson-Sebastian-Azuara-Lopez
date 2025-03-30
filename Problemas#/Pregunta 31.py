# Pregunta 31
#print(int(3.999))
#print(float(3.1416))
#print(str(2.71))

#import math
#print(math.pi)

#import random

#for i in range(10):
   # x = random.random()
    #print(x)

#t = [1,5,10,1,31,42.,64,84,68,46]
#print(random.choice(t))

#n = 5
#while n > 0:
 #   print(n)
 #   n = n - 1
#print("despegue")

#palabra = "banana"
#contador = 0
#for letra in palabra:
#    if letra == "a":
#        contador = contador + 1
#        print(contador)

#print(type(t))


#a = {"name": "apple", "color": "green"}

#my_list = [10,20,30,40]
#my_list.pop(0)
#print(my_list)

#fruits = ["apple", "banana", "cherry"]



#import math 

#import random 
#print(random.randint(1, 10))

#def invertir_cadena(cadena):
#    ----invertir_cadena(str(cadena))

# palabra = brontosaurio
#d = dict()
#for c in palabra:
#        if c not in d:
#            d[c] = 1
#        else:
#            d[c] = d[c] + 1
#            print(d)
#
#número = input(int())
#print(número)
#while número > 10:
#      print(número)
#      número = número / 10

#narchivo = input('ingresa un numbre de archivo: ')
#man_a = open(narchivo)
#contador = 0
#for linea in man_a:
#    if linea.startswith('subject:'):
#        contador = contador + 1
#print('Hay', contador, 'líneas de asunto (subject) en', narchivo)
import random

#for i in range(100):
#    x = random.random()
#    print(x)

#t = [0,1,2,3,4,5,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#print(random.choice(t))

#def muestra_estribillo():
     #print("Soy un leñador, qué alegría.")
     #print("Duermo toda la noche y trabajo todo el día.")

#muestra_estribillo()
    
#def repite_estribillo():
    #muestra_estribillo()
    #muestra_estribillo()

#repite_estribillo()

#def sumados(a, b):
#    suma = a + b
#    return suma

#x = sumados(19, 29)
#print(x)

#def fred():
#    print('Zap')
#def jane():
#    print('ABC')

#jane()
#fred()
#jane()

#def calcula_calificación():

#x = 0
#x = x + 1

#print(x)

#while True:
#    linea = input('>')
#    if linea == 'fin':
#        break
#    print(linea)
#print('terminado')

#while True:
#    operación = input('multipicación de 40 x 100 = ')
#    if operación == '4000':
#        break
#    print(operación)
#print('verdad')

#while True:
#    línea = input('>')
#    if línea[0] == '#':
#        continue
#    if línea == 'fin':
#        break
#    print(línea)
#print('Terminado')

#def cuestionario():

#    while True:
#        línea = input('¿Cúal es el mejor país del mundo? ')
#        if línea == 'México':
#            print('A huevo')
#        else:
#            print('Maleta¡¡¡¡')
#        línea = input('¿Cuán basado estoy? a)Bien basado, b)Tas pendejo')
#        if línea == 'a':
#                print('¡¡¡Con madre pasaste¡¡¡')
#        else:
#            print('Maleta¡¡¡¡')
#        break
#    print('')

#respuesta = input('¿Desea comenzar el cuestinario?' )
#if respuesta == 'Sí':
#    cuestionario()
#else:
#    print('Ni modo')

#amigos = ['Pablo','Carolina','Fernando','Rodigo','Belinda','Alex','Gael','Suzeth']
#for amigo in amigos:
#    print('Feliz año nuevo', amigo)
#print('feliz año nuevo a todos')

#contador = 0
#for valor in [3, 41, 12,9, 74, 15]:
#    contador = contador + 1
#print('num. elementos', contador)

#contador = 0
#for valor in [3, 5, 6, 100, 34, 64]:
#    contador = contador + 1
#print('num. elemntos', contador)

#Mayor = None
#print('Antes:', Mayor)
#for valor in [7,5345,77423,6784,445677,4322,67653,4676,4324,66,75433,]:
#    if Mayor is None or valor > Mayor:
#        Mayor = valor
#    print('Bucle:', valor, Mayor)
#print('Mayor:', Mayor)

#print('Calificaciones de prepratoria')
#Mayor = None
#for valor in [94,95,34,65,86,78,36,36,26,8,42,46,88,66,21,75,78,44,99,6,4,22,76,52,98,86,96]:
#    if Mayor is None or valor > Mayor:
#        Mayor = valor
#    print('Bucle:', valor, Mayor)
#print('Mayor:', Mayor)

#Escribe un programa que lea repetidamente números hasta
 #que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
 #muestra por pantalla el total, la cantidad de números y la media de
 #esos números. Si el usuario introduce cualquier otra cosa que no sea un
 #número, detecta su fallo usando try y except, muestra un mensaje de
 #error y pasa al número siguiente.

#def repeitr_numeros():
#    while True:
#        número = input('ingrese un número:' )
#        if número == int():
#            print(número)
#        else:
#            print('error')

#número = 10
#while número > 0:
#      print(repeitr_numeros())
#      número = número - 1

#Ejercicio 2: Escribe otro programa que pida una lista de números como
 #la anterior y al final muestre por pantalla el máximo y mínimo de los
 #números, en vez de la media.

#mayor = None
#print('Antes:', mayor)
#for valor in [1,4,64,74,47,32,56,532,64,233,46,675,234,67,765,244,567,442,447,764]:
#    if mayor is None or valor > mayor:
#        mayor = valor
#    print('Bucle:', mayor, valor)
#print('Y el número más grande e la lista es.......: ', mayor)

#Menor = None
#print('Antes:', Menor)
#for valor in [3,7,5,5,7,8,12,15,16,13,14,14,17,17,19,2,4,21,3,4,56,54.78]:
#    if Menor is None or valor < Menor:
#        Menor = valor
#    print('bucle:', valor, Menor)
#print('Y la que se va a dar el Dallas es......', Menor)

#def min(valores):
#    Menor = None
#    for valor in valores:
#        if Menor is None or valor < Menor:
#            Menor = valor
#        return Menor

# Ejercicio 1: Escribe un programa que lea repetidamente números hasta
 #que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
 #muestra por pantalla el total, la cantidad de números y la media de
 #esos números. Si el usuario introduce cualquier otra cosa que no sea un
 #número, detecta su fallo usando try y except, muestra un mensaje de
 #error y pasa al número siguiente.

 #contador = 0
#for valor in [3, 5, 6, 100, 34, 64]:
#    contador = contador + 1
#print('num. elemntos', contador)

#contador = 0
#valores = input('introduzca valores: ', )
#while valores == (str('fin')):
#    print(contador)
#    print('fin')
#else:
#    contador = contador + 1

#print("Vamos a ver quien es el más pendejo, según yo son: ")
#Pendejos = ["Tú", "Pablo", "Rod", "Fer", "Caro", "Lusimi", "Belinda", "Walter", "Aldo", "Max", "Suzeth", "Brriones", "El wero"]
#print(random.choice(Pendejos))

#import math

#print(math.sqrt(2025))

# Conjuntos

#mensaje = "Jhon stuart mill es un pendejo de primera"
#print(mensaje.capitalize())
#print(mensaje.count('e'))

#boludo = 'esrdtfyguhiml dcgyguahxickn fmvehcsjnk mfbnrvhefwcjaxnk cfbjvdnkcs xm'
#print(boludo.count('u'))

#with open("pejelagarto.txt","w",encoding='utf8') as file:
#    print(mensaje, file=file)

#with open('pejelagarto.txt', 'r', encoding= 'utf8') as fichero:
#    print(fichero.readlines())

#print(mensaje.index('a'))

#indicesE = []


#for indice in range(len(mensaje)):
#    if mensaje[indice] == 'e':
#        indicesE.append(indice)
#    print(mensaje[indice], end=" ")
#print(indicesE)

#print(len(mensaje))

#mensaje = 'si sale cinco te la comes, además de que la piche ilustración fue en relalidad una aberración de la cual deberíamos como humnanidad estar arrepentidos, pero al étile masónico judeía-anglosajona lo impedirá, así como han impedido la reunificación hispana.'

#print(mensaje.count('a'))
#print(mensaje.endswith('hispana'))
#print(mensaje.startswith('si'))

#print(mensaje.find('judeía-anglosajona'))

#import math
#print('{:.8}'.format(math.pi))

#Mensaje = 'el profe es un pendejo'

#print(Mensaje.capitalize())
#print(Mensaje.count(' '))

#Listas
#Nombres = ['Panamá', 'Paraguay', 'Perú', 'República Dominicana', 'Uruguay','Venezuela']
#Notas = [88, 89, 80, 87, 98, 64]

#for Nombre, Notas in zip(Nombres, Notas):
#    print(f"{Nombre} obtuvo {Notas}")
#for i in enumerate(Nombres):
#    print(i)

#def multiplicación_por_dos(número):
#    return número * 2
#números = [1,2,3,4,5,6,7,8,9,10]
#resultado = list(map(multiplicación_por_dos, números))
#print(resultado)

#def población_en_cien_años(número):
#    return número * (3/2)
#poblaciones = [126, 40, 35, 45, 205, 16]
#resultado = list(map(población_en_cien_años, poblaciones))
#print(resultado)

#números = [5,12,7,20,43,56]
#esultado = list(map(lambda x: x * 2, números))
#print(resultado)

#números = [5,3,5,7,6,45,3,22,54]
#def es_mayor_que_10(número):
#    return número > 10
#resultado = list(filter(es_mayor_que_10, números))
#print(resultado)

#Provicias = ['Nueva España', 'Nueva Granada', 'Perú', 'Rio de la Plata', 'Brasil', 'España', 'Otros dominios', 'Fillhipinas']
#poblaciones = [230, 150, 60, 70, 200, 50, 8, 110]

#for provincia, poblaciones in zip(Provicias, poblaciones):
#    print(f"{provincia} Tiene en 2025 {poblaciones}")
#for i in enumerate(Provicias):
#    print(i)

#tupla = tuple()

#poblaciones = [10, 6, 6, 4, 4]
#def suma2(a, b, c=0):
#    return a+b+c

#class sumatoria():
#    def __init__(self, lista=[0]):
#        self.n = len(lista)
#        self.sum = sum(lista)
#        print("hola mundo")
    
#    def getSum(self):
#        return self.sum
    
#    def getProm(self):
#        return self.getSum()/self.n
    
#demo = sumatoria()
#demo2 = sumatoria(poblaciones)

#print(demo.getSum(), demo2.getSum, demo2.getProm())

from abc import ABC, abstractmethod
class Politopo2(ABC)


def area(self):
    pass

def perimetro(self):
    pass

class Cuadrado(Politopo2):
    def __init__(self, NombreFigura=Nombre):
        self.lado = 1
        super(). __init__(self, NombreFigura=Nombre)
