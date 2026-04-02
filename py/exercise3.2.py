import random

score = 0
for i in range(3):
    num1 = random.randrange(1, 100)
    num2 = random.randrange(1, 100)
    result = num1 + num2

    while True:
        try:
            answer = int(input(f"{num1} + {num2}: "))
            break
        except ValueError:
            print("Please enter a valid integer")
    
    if result == answer:
        score += 1

print(f"Your score is: {score}")