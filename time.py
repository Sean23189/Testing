import datetime

while True:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-5]
    print(f"\rThe current time is: {current_time}", end = "")
