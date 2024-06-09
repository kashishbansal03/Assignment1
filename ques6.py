
file_name = "txt1.txt"
try:
    with open(file_name, "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
