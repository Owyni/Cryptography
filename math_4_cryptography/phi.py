from module import mod

n = int(input("Ingrese un número para calcular su Φ: "))

def gcd(a, b):
    while b != 0:
        a, b = b, mod(a, b)
    return a

def phi(a):
    coprimo = 0
    for i in range(1, a + 1):
        if gcd(a, i) == 1:
            coprimo += 1
    return coprimo

print("Φ de " + str(n) + " es: " + str(phi(n)))
