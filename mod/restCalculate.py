firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

def mod(a,b):
    c = a / b
    residuo = a - (int(c) * b)
    return residuo
    
print(mod((firstNumber), (secondNumber)))