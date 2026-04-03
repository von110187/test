import random

list = [random.randrange(1, 100) for i in range(10)]

print(list)

largest = max(list)
smallest = min(list)
print(f"Largest: {largest}, Smallest: {smallest}")