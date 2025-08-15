firstNumber = int(input())
secondNumber = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
print(gcd(firstNumber, secondNumber))