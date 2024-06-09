def factorial(n):
    if n < 0:
        return "factorial is not defined for negative numbers"
    
    if n == 0 or n == 1:
        return 1
    
    else:
        result = 1
        for i in range(2,n+1):
            result *= i
        return result
    
num = int(input("Enter the number"))
result = factorial(num)
print(result)

