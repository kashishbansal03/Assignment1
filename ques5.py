
user_input = input("Enter the string you want to write to the file: ")

file_name = "output.txt"
with open(file_name, "w") as file:
    file.write(user_input)

print(f"The string has been written to {file_name}.")
