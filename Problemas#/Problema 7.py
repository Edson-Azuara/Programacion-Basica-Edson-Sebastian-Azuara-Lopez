#problema 7
def función_general():
    a = print(input('ingrese el valor de a: '))
    b = print(input('ingrese el valor de b: '))
    c = print(input('ingrese el valor de c: '))
    d = (b * b)
    print( d + (4 * a * c))
    if función_general > 0:
        print((-b + ( d + (4 * a * c))^(1/2))/2)
        print((-b - ( d + (4 * a * c))^(1/2))/2)
