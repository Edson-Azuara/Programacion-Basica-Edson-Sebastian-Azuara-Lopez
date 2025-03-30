# Problema 34

matirz1 = ((2,3),(4,3))

a1b1 = 2
a1b2 = 3

a2b1 = 4
a2b2 = 3

Dtereminate = (a1b1 * a2b2) - (a2b1 * a1b2)


def matriz_inversa():
    Ba1b1 = a1b1/Dtereminate
    Ba1b2 = (a1b2/Dtereminate) * (-1)
    Ba2b1 = a2b1/Dtereminate
    Ba2b2 = a2b2/Dtereminate * (-1)
    print(Ba1b1)
    print(Ba1b2)
    print(Ba2b1)
    print(Ba2b2)

matriz_inversa()