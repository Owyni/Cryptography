from module import mod

inv_a = int(input("Número a invertir (inv_a): "))
m = int(input("Módulo (m): "))

def calc_inv(a, m):
    for i in range(1, m):
        if mod((a * i), m) == 1:
            return i
    return None

resultado = calc_inv(inv_a, m)

if resultado:
    print(f"El inverso modular de {inv_a} mod {m} es: {resultado}")
else:
    print(f"No existe inverso modular de {inv_a} mod {m}")
