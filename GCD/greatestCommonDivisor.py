a = int(input("Primer número: "))
b = int(input("Segundo número: "))

# Algoritmo de Euclides
while b != 0:
    temp = b
    b = a % b
    a = temp

print(a)