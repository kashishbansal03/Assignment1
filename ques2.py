def checkNumber(num):
    if num%2 == 0:
        return "Number is even"
    else:
        return "Number is odd"
    


num = int(input("Enter number"))
result= checkNumber(num)
print(result)
