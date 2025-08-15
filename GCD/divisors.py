number = int(input())

divisors = [
    i for i in range(1, int(number) + 1) if int(number) % i == 0
]

print(divisors)