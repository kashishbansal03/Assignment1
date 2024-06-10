def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

input_list = input("Enter elements of the list separated by spaces: ").split()

my_list = [int(x) for x in input_list]

element_to_count = int(input("Enter the element you want to count: "))

occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list.")
