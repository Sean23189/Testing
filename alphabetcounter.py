import time

def increment_alphabet(curr_str):
    if not curr_str:
        return 'a'
    
    last_char = curr_str[-1]
    if last_char == 'z':
        return increment_alphabet(curr_str[:-1]) + 'a'
    else:
        return curr_str[:-1] + chr(ord(last_char) + 1)

current_value = ''
start_time = time.time()
update_interval = 1  # Update progress every 1 second
last_update_time = start_time

with open('alphabet_entries.txt', 'w') as file:
    while True:
        if current_value != '':
            file.write(current_value + '\n')
        if current_value == 'zzzzz':
            break
        current_value = increment_alphabet(current_value)

        current_time = time.time()
        if current_time - last_update_time >= update_interval:
            elapsed_time = current_time - start_time
            print(f"Generating entries... Elapsed time: {elapsed_time:.2f} seconds", end='\r')
            last_update_time = current_time

end_time = time.time()
elapsed_time = end_time - start_time

# Remove extra empty line at the start of the file
with open('alphabet_entries.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip()]

with open('alphabet_entries.txt', 'w') as file:
    file.write('\n'.join(lines))

print("\nAlphabet entries generated successfully.")
print(f"Total time taken: {elapsed_time:.2f} seconds.")
