num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

while True:
    try:
        operation = input("Operation (+-*/): ")
        if operation == "+":
            result = num1 + num2
            break
        elif operation == "-":
            result = num1 - num2
            break
        elif operation == "*":
            result = num1 * num2
            break
        elif operation == "/":
            result = num1 / num2
            break
        else:
            print("Operation must be +-*/")
    except ValueError:
        print("Please enter a valid operation!")

print(f"Answer: {result}")