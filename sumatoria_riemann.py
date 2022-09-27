from time import time
import multiprocessing as mp
from tkinter import N

sumatoria = 0

def calcular_area(li, ls, x, parts, step):
    b = (ls - li) / parts
    
    for _ in range(li, ls, step):
        a = eval(funcion)
        area = b * a
    return area


if __name__ == "__main__":
    tiempo_actual = time()
    funcion = "x**3 + x**2 + 2*x"
    li, ls = 1, 10
    parts = 1_000_000
    x = li + ((ls - li)/parts)

    resultado = 0

    n = mp.cpu_count()
    
    pool = mp.Pool()
    resultados = [pool.apply_async(calcular_area, args=(li, ls, x, parts n)) for i in range(n)]

    for result in resultados:
        resultado += result.get()

    print("RESULTADO: ",resultado)
    print("Se tardó: ", time() - tiempo_actual)