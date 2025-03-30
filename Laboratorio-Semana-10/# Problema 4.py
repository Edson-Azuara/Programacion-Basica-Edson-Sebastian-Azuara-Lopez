# Problema 4
 #Crea una funci´on que reciba una lista de n´ umeros y devuelva:
 #Promedio, mediana y desviaci´on est´andar.
 ##Utilizar funciones lambda para c´alculos simples como la media.
 #El programa debe solicitar al usuario una lista de n´ umeros y mostrar los resul
 #tados.

import statistics

def calcular_estadisticas(*args):
    if not args:
        return "No se proporcionaron números."
    
    promedio = lambda numeros: sum(numeros) / len(numeros)
    mediana = statistics.median(args)
    desviacion = statistics.stdev(args) if len(args) > 1 else 0
    
    return promedio(args), mediana, desviacion

