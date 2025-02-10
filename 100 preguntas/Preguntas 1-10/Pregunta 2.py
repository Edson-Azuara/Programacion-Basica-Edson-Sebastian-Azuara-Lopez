#Actividad 2

from fractions import Fraction
from decimal import Decimal
# Se declara si es fracción o decimal.

a = 1 #int(input("Ingrese el primer número: "))
b = 5 #int(input("Ingrese el segundo número: "))
# Se ingresan los números

print("adición=", a + b)
print("sustracción=", a - b)
print("multipicación=", a * b)
print("división=", Fraction(Decimal(a) / Decimal(b)))
#Se realizan las operaciones
