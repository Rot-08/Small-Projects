import time

try:        
    mins = int(input("Enter Number of Minutes: "))
    secs = int(input("Enter Number of Seconds: "))
    if secs > 60:
        raise Exception

    while mins >= 0:
        
        print(mins, " : ", secs)
        time.sleep(1)
        secs -= 1
        if secs == 0:
            mins -= 1
            secs = 59

    print("Time Up")        
except Exception as e:
    print("Invalid Entry")