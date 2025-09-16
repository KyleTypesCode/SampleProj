import datetime 
import zoneinfo
import time
import webbrowser


tz = zoneinfo.ZoneInfo("Asia/Hong_Kong")
DateTime = datetime.datetime.now(tz)
currentTime = DateTime.time()
ShiftStatus = ""
log_Status = ""


def checkIfWeekday():
    WeekdayCheck = DateTime.weekday() < 5
    return WeekdayCheck == True
       

def compareTime():
    #Variable Initialzation
    log_Status = "Logged Out"
    ShiftStatus = "Pre-Shift"
    UpdTime = datetime.datetime.now(tz)
    StrUpdTime = UpdTime.strftime('%c')
    #Range
    TimeBefore = datetime.datetime(2025, 9, 15, 9, 0, 0)
    TimeAfter = datetime.datetime(2025, 9, 15, 18, 3, 0)
    result =  TimeBefore.time() < UpdTime.time() < TimeAfter.time()  
    
    #Conditions
    if TimeBefore.time() > UpdTime.time():
        print(ShiftStatus)
        Status = input("Have you logged in ATGS? Yes or No: ")
        if Status == "Yes":
            log_Status = "Logged In"
            print (log_Status)
        elif Status == "No":
            print ("Please log in now")
            time.sleep(3)
            webbrowser.open('https://app.atgspay.com/app/user-dashboard')
    elif UpdTime.time() > TimeAfter.time():
        ShiftStatus = "Post-Shift"
        print(ShiftStatus)
        Status = input("Have you logged out of ATGS? Yes or No: ")
        if Status == "Yes":
            log_Status == "Logged Out"
            print (log_Status)
            return True
        elif Status == "No":
            print ("Please log out now")
            time.sleep(3)
            webbrowser.open('https://app.atgspay.com/app/user-dashboard')
    else:
        ShiftStatus = "On-Shift"
        print(ShiftStatus)

    print(f"The time is now: {UpdTime} ")
    return result

        
def main():
    if checkIfWeekday():
        while compareTime():
            time.sleep(1)
    else:
        print("default")


if __name__ == "__main__":
    main()