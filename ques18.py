def are_anagrams(string1, string2):
    cleaned_string1 = ''.join(string1.split()).lower()
    cleaned_string2 = ''.join(string2.split()).lower()
    return sorted(cleaned_string1) == sorted(cleaned_string2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
