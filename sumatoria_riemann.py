from time import time

funcion = "x**3 + x**2 + 2*x"
li, ls = 1, 10
parts = 1_000_000
interval = (ls - li) / parts
x = li + (interval/2) #valor del punto medio y primer valor de X.

sumatoria = 0

tiempo_actual = time()

for _ in range(parts):
    fx = eval(funcion)
    sumatoria += (interval * fx)
    x = x + interval

print("Se tardó: ", time() - tiempo_actual)