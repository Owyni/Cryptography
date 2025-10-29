from module import mod

def calc_inv(a, m):
    for i in range(1, m):
        if mod((a * i), m) == 1:
            return i
    return None