import module
from module import mod

n = int(input("Ingrese un número para calcular su Φ: "))

def phi(a):
    coprimo = 0
    for i in range(1,a):
        if mod(a, i) == 0:
            coprimo += 1
    return coprimo

print("Φ de " + str(n) + " es: " + str(phi(n)))