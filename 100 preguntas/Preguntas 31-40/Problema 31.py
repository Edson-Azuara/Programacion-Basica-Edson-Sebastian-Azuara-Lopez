# problema 31


def factorial():
    n = input()
    if n == 0:
        return 1
    else:
        recursivo = factorial(n - 1)
        resultado = n * recursivo
        print(resultado)
    return resultado

