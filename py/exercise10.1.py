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
        user_input = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid integer")

if is_prime(user_input):
    print(f"{user_input} is a prime number")
else:
    print(f"{user_input} is not a prime number")