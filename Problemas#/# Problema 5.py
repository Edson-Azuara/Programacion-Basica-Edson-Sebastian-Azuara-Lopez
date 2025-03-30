# Problema 5

 #Crea un m´odulo de Python llamado conversor.py que contenga funciones para
 #convertir:

 #Kil´ometros a millas.
 #elsius a Fahrenheit.
 #Litros a galones.
 #Luego, crea un programa principal que importe el m´odulo y permita al usuario
 #realizar conversiones.

def convertir_km_millas():
    Kilometros = input('Ingese kiómetros: ')
    millas = Kilometros/1.69
    print(millas)

def converit_Celsius_Farenhait():
    celsius = input('Ingrese grados: ')
    Farenhait = ((celsius + 32)/1.8)
    print(Farenhait)

def litros_galones():
    litros = input('Ingrese litros: ')
    galones = litros/0.4
    print(galones)

