
str = input("Enter the main string: ")
substr = input("Enter the substring to check: ")
if substr in str:
    print(f"The substring '{substr}' is present in the main string.")
else:
    print(f"The substring '{substr}' is not present in the main string.")
