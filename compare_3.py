num1 = float(input("Enter 3 seperate numbers: "))
num2 = float(input())
num3 = float(input())

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3}.")

elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater than {num1} and {num3}.")

else:
    print(f"{num3} is greater than {num1} and {num2}.")