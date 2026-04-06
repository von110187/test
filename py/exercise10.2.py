def cel_to_fah(c):
    fahrenheit = c * 9 / 5 + 32
    return fahrenheit

while True:
    try:
        user_input = float(input("Enter a temperature(celcius): "))
        break
    except ValueError:
        print("Please enter a valid integer")

print(f"\nFahrenheit: {cel_to_fah(user_input)}")