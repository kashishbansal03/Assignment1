def read_multiple_lines():
    lines = []
    print("Enter multiple lines of text (press Enter on an empty line to finish):")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    return lines

def print_lines(lines):
    print("\nYou entered:")
    for line in lines:
        print(line)

lines = read_multiple_lines()
print_lines(lines)
