import time
from scheduler import Scheduler
from clock import Clock
from apps import Apps
from pomodoro import Pomodoro
from time_set import TimeSet
APP_CLASSES = [
    Clock,
    Pomodoro,
    TimeSet,
]
from rtc import RTC
clock=RTC()
scheduler = Scheduler()
apps = Apps(scheduler)
for App in APP_CLASSES:
    apps.add(App(scheduler))
import machine
print("STARTING...")
scheduler.start()

while True:
    v=input("enter command\n")
    try:
        w, YY, MM, mday, hh, mm, ss, wday, yday = v.split(",")
        print(w)
        print(YY)
        v=w    
    except:
        print ("fail")
        pass
    if (v == "set"):
            print("set")
            t=(int(YY), int(MM), int(mday), int(hh), int(mm), int(ss), int(wday), int(yday))
            print (t)
            clock.save_time(tuple(t))
            machine.reset()
    if (v == "get"):
        print (clock.get_time())
        
    time.sleep(1)
    
