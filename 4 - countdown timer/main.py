import time


def coundown(time_entered):
    while time_entered:
        mins, secs = divmod(time_entered, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_entered -= 1
    print("Time's up!")


if __name__ == '__main__':
    time_entered = input("Enter the time in seconds: ")
    coundown(int(time_entered))
