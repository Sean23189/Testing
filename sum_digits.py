pint = str(input("Please enter a positive integer: ")) # pint means positive integer

if int(pint) <= 0:
    print("Please enter an integer greater than 0")

else:
    sumdigits = 0
    for num in pint:
        sumdigits += int(num)
    print (sumdigits)
