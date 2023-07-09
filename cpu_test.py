import time

start_time = time.time()
count = 0

while True:
    count += 1
    
    if time.time() - start_time >= 1.0:
        break

print("Operations in a single second:", count)
