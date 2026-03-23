import time

while True:
    try:
        seconds = int(input("How many seconds should the countdown start from: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if seconds <= 0:
        print("Please enter a positive number")
        continue

    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
        if seconds == 0:
            print("Time's Up")

    again = str(input("Do you want another countdown Y/N: ")).lower()
    if again == "n":
        break