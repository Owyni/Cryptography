# Solicita dos números al usuario
a = int(input("Primer número: "))
b = int(input("Segundo número: "))

# Calcula el máximo común divisor usando el algoritmo de Euclides paso a paso
while b != 0:
    temp = b
    b = a % b
    a = temp

print(a)