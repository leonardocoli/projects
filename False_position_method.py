from math import *
import math

a = 0
b = 2
f = lambda x: 1 - (2 * x * (math.e**(-x / 2))) - x * math.sin(x)


def False_position_method(f,a,b,nmax,tol):
    i=1

    fb = f(b)
    fa = f(a)

    if fa * fb > 0:
        raise Exception("o intervalo [A,B], nao satisfaz a condicao de convergencia")

    while i <= nmax:
        x = a - (((b - a) - (fa)) / (fb - fa))
        fx = f(x)

        if abs(fx) < tol or a == x:
            return x
        else:
            i += 1

            if fx*fb < 0:
                a = x
            else:
                b = x


        print( f"Iteration {i}: a = {a}, b = {b}, x = {x}, fx = {fx}")

    raise Exception("Você ultrapassou o número máximo de iterações do programa")

#valores de entrada

tol = 1e-5
nmax = 100

raizfuncao = False_position_method(f, a, b, nmax, tol)
print(raizfuncao)

