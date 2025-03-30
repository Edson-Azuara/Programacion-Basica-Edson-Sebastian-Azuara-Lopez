# Prolema 9

#Desarrolla un programa que implemente diferentes paradigmas de programaci´on:
 #Imperativa: Uso de estructuras de control como condicionales y bucles.
 #Estructurada: Separar el c´odigo en funciones bien definidas.
 #Modular: Crear diferentes m´odulos para funcionalidades espec´ ıficas.
 #Orientada a Objetos: Definir clases y objetos.
 #El programa debe demostrar el uso de cada paradigma con ejemplos claros


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else 'Error: División por cero'


class Calculadora:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial
    
    def sumar(self, cantidad):
        self.valor += cantidad
    
    def restar(self, cantidad):
        self.valor -= cantidad
    
    def mostrar_valor(self):
        print(f'Valor actual: {self.valor}')


def ejecutar_calculos():
    numero1 = 10
    numero2 = 5
    
    print("Suma:", suma(numero1, numero2))
    print("Resta:", resta(numero1, numero2))
    print("Multiplicación:", multiplicacion(numero1, numero2))
    print("División:", division(numero1, numero2))
    

    for i in range(3):
        print(f"Iteración {i+1}")
    
    if numero1 > numero2:
        print("Número1 es mayor que Número2")
    else:
        print("Número2 es mayor o igual a Número1")


def main():
    print("Ejecutando cálculos...")
    ejecutar_calculos()
    
    print("\nUsando la clase Calculadora")
    calc = Calculadora()
    calc.sumar(15)
    calc.restar(5)
    calc.mostrar_valor()

if __name__ == "__main__":
    main()
