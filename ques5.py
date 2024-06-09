# Prompt the user to enter a string
user_input = input("Enter the string you want to write to the file: ")

# Specify the name of the file
file_name = "output.txt"

# Open the file in write mode and write the user's input to it
with open(file_name, "w") as file:
    file.write(user_input)

print(f"The string has been written to {file_name}.")
