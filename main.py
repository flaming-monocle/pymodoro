# a basic pomodoro timer application for Python
import time

def main():
    print("Welcome to pymodoro, my first Python app.")
    print("Customize your timer now.")
    
    # Get user-defined intervals
    sWork, sRest = timerInput()

    workFlip(sWork, sRest)

def timerInput():
    inputStatus = 0

    # Takes user input for timing
    while inputStatus == 0:
        mTimeWork = int(input("Work time in minutes: "))
        mTimeRest = int(input("Rest time in minutes: "))

        # print(type(mTimeRest))

        # Checks input
        if type(mTimeWork)!=int or type(mTimeRest)!=int:
            print("This app only supports whole numbers, please enter the time as an integer.")
        else: 
            inputStatus = 1
    sTimeWork = mTimeWork * 60
    sTimeRest = mTimeRest * 60

    print("You've set up a pomodoro timer that'll have " + str(mTimeWork) + "-minute work periods, interspersed by " + str(mTimeRest) + "-minute rest periods.")

    return sTimeWork, sTimeRest

def workFlip(sWork, sRest):
    print("The timer will loop between work and rest until you stop running the program with Ctrl-C")
    

    while True:
        print("Working!")
        countdown(sWork)
        print("Resting :)")
        countdown(sRest)
        print("Remember, you can cancel this timer with Ctrl-C")

def countdown(t):
    # time acceleration factor for fast debugging
    timescale = 10
    # print(t)

    max = int(t/60)

    while t >= 0:
        min, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end = "\r")
        time.sleep(1/timescale)
        t -= 1
    print(str(max) + "-minute interval done!")
    return

main()