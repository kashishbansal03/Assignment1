def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ").upper()

if unit == 'C':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {converted_temperature}°F.")
elif unit == 'F':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {converted_temperature}°C.")
else:
    print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")