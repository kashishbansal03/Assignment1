import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = input_string.translate(translator)
    
    return cleaned_string

input_string = input("Enter a string: ")
cleaned_string = remove_punctuation(input_string)

print("String without punctuation:")
print(cleaned_string)
