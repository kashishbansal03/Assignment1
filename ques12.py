def sum_of_digits(number):
    number = abs(number)
    digits = str(number)
    sum_digits = sum(int(digit) for digit in digits)
    
    return sum_digits

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")
