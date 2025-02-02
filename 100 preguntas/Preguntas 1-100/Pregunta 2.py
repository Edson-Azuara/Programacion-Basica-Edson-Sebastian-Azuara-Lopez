#Actividad 2
from fractions import Fraction
from decimal import Decimal

a = 1 #int(input("Ingrese el primer número: "))
b = 5 #int(input("Ingrese el segundo número: "))

print("adición=", a + b)
print("sustracción=", a - b)
print("multipicación=", a * b)
print("división=", Fraction(Decimal(a) / Decimal(b)))

