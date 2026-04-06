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
        user_input = int(input("Find primes within: "))
        break
    except ValueError:
        print("Please enter a valid integer")

result = []
count = 0

for num in range(2, user_input + 1):
    if count >= 20:
        break
    if is_prime(num):
        result.append(num)
        count += 1

if len(result) > 0:
    print(f"Result: {result}")
else:
    print(f"No Prime number in {user_input}")