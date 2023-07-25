import datetime
from playsound import playsound
alarmhour=int(input("enter hour:"))
alarmmin=int(input("enter minutes:"))
alarmAM=input("am/pm:")
if alarmAM=="pm":
    alarmhour=alarmhour+12
    while True:
        if alarmhour==datetime.datetime.now().hour and alarmmin == datetime.datetime.now().minute:
            print("playing......")
            playsound(r"C:\Users\chand\Desktop\as.mp3")
            break
