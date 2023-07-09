def count_up(target_number):
    for num in range(1, target_number + 1):
        print(num)

# Prompt the user for the target number
target = int(input("Enter the target number: "))

# Call the function to count up
count_up(target)
