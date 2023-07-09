num = 0

while True:
    num += 1

    # Calculate the number of separators needed based on the length of the number
    separators = (len(str(num)) - 1) // 3

    formatted_num = "{:,}".format(num)  # Format the number with thousands separators
    print(f"\r{formatted_num}{' ' * separators}", end="", flush=True)
