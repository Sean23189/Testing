keyword = "done"
nums = []
average = 0


def calc_average(nums):
    total = 0
    divider = len(nums)
    for num in nums:
        total += num
    global average
    average = total / divider
    return average


print("Enter your numbers 1 by 1 and type 'done' to finish: ")
run = True
while run == True:
    user_input = input()
    if user_input != keyword:
        nums.append(int(user_input))

    else:
        calc_average(nums)
        run = False

else:
    print(average)
