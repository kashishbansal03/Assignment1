def convert_to_title_case(input_string):
    title_case_string = input_string.title()
    return title_case_string

input_string = input("Enter a string: ")
title_case_string = convert_to_title_case(input_string)

print("Title case string:")
print(title_case_string)
