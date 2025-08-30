# Solicita al usuario un número entero
number = int(input("Ingrese un número: "))

divisores = []

for i in range(1, number + 1):
    # Reviso si i es divisor exacto del número
    if number % i == 0:
        divisores.append(i)

print(divisores)