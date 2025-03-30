# Problema 6

#Crea una clase Vehiculo con los siguientes atributos y m´ etodos:

 #Atributos: marca, modelo, a˜ no y precio.
 #M´etodo para mostrar la informaci´on del veh´ ıculo.
 #Crear subclases Automovil y Motocicleta con atributos adicionales como
 #n´ umero de puertas o cilindrada.

class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro1 = vehiculo('Volzwaguen', '1')
carro2 = vehiculo('Tesla', 'Model 3')

print(carro1.marca, carro1.modelo)
print(carro2.marca, carro2.modelo)

