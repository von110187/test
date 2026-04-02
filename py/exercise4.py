while True:
    try:
        weight = float(input(f"Weight(kg): "))
        height = float(input(f"Height(m): "))
        break
    except ValueError:
        print("Please enter a number")

bmi = weight / height ** 2

if bmi < 18.5:
    category = "underweight"
elif bmi < 24.9:
    category = "normal weight"
elif bmi < 29.9:
    category = "overweight"
else:
    category = "obesity"

print(f"\nYour BMI is: {bmi:.1f}")
print(f"Category: {category}")