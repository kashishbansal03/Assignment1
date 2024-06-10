def starts_with_prefix(string, prefix):
    return string.startswith(prefix)

def ends_with_suffix(string, suffix):
    return string.endswith(suffix)

my_string = input("Enter a string: ")
prefix = input("Enter a prefix: ")
suffix = input("Enter a suffix: ")

starts_with = starts_with_prefix(my_string, prefix)
ends_with = ends_with_suffix(my_string, suffix)

print(f"Does the string '{my_string}' start with the prefix '{prefix}'? {starts_with}")
print(f"Does the string '{my_string}' end with the suffix '{suffix}'? {ends_with}")
