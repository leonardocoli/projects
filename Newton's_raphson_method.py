
from math import *
import math


f = lambda x: 1 - (2 * x * (math.e**(-x / 2))) - x * math.sin(x)
df = lambda x: -x * cos(x) + x * exp(-x/2) - sin(x) - 2 * exp(-x/2)


a = 0
def Newton_Raphson_method(f,df, a,nmax,tol):
    i = 1
    fa = f(a)
    dfa = df(a)


    while i <= nmax:
        x = a - (f(a)) / (df(a))

        fx = f(x)
        dfx = df(x)

        if abs(x) < tol or x == a:
            return x
        else:

            i += 1

            a = x

        print(f"Iteration {i}: a = {a}, dfx = {dfx}, x = {x}, fx = {fx}")

    raise Exception("iteration num trapassed")

tol = 1e-6
nmax = 100


raizfuncao = Newton_Raphson_method(f, df, a, nmax, tol)
print(raizfuncao)
