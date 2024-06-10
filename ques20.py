def calculate_sum(numbers):
    return sum(numbers)

input_numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in input_numbers]  
total_sum = calculate_sum(numbers)

print("Sum of the numbers:", total_sum)
