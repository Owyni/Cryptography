import random
from inv import calc_inv


p = int(input("Inserte número primo: "))
g = int(input("Inserte número generador: "))
m = int(input("Ingrese m: "))

a = 3
b = 6

llave_a = (g**a) % p
llave_b = (g**b) % p
llave_ab = (g**a)**b

c = m*llave_ab % p

try:
    m_desencriptada = c * calc_inv(llave_ab, p) % p
except TypeError:
    print("El generador ingresado no tiene inversa")


print(m_desencriptada)