def factorial(num):
    result = 1
    while num >= 1:
        result *= num
        num -= 1

    return result
    
num = int(input("Enter the number you want to get the factorial of: "))      
result = factorial(num)
print(f"The factorial of {num} is {result}")