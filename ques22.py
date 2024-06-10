def min_max(lst):
    if not lst:
        return None, None  
    min_value = max_value = lst[0]  
    for num in lst:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num
    return min_value, max_value

input_list = input("Enter numbers separated by spaces: ").split()

my_list = [int(x) for x in input_list]

min_value, max_value = min_max(my_list)
print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")
