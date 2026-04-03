import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
        try:
            input = int(input("Find primes for: "))
            break
        except ValueError:
            print("Please enter a valid integer")

for num in range(2, input + 1):
    if is_prime(num):
        print(num)