import restCalculate
from restCalculate import mod

inv_a = int(input("inv(_) : "))
m = int(input("Escribe el modulo: "))

def calc_inv(inv):
    for i in range(m - 1):
        for j in range(m -1):
            if mod((inv_a * i), (m * j)) == 1:
                inv = (inv_a * i)
                return inv
                break


print(calc_inv)