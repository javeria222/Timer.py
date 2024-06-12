import time

def timer(time_sec):
    while time_sec:
        minutes, seconds = divmod(time_sec, 60)
        timeformat = "{:02d}:{:02d}".format(minutes, seconds)
        print(timeformat, end="\r")
        time.sleep(1)
        time_sec -= 1

timer(70)