#To change time, set second, minute, and hour to a value

import math
import time
import os

#Change these values to get the correct time
second = 0
minute = 0
hour = 12

#For AM, change value to 1. For PM, change value to 2
am_pm = 1

#You may change these values, but does not do anything
str(second) == 0
str(minute) == 0
str(hour) == 12

while True:
    __import__('os').system('clear')
    print(hour,":",f"{minute:02}",":",f"{second:02}")
    if am_pm == 1:
      print("AM")
    else:
      print("PM")
    
    second = int(second) + 1
    if second == 60:
      second = 0
      second = f"{second:02d}"
      minute = int(minute) + 1
    if minute == 60:
      minute = 0
      minute = f"{minute:02d}"
      hour = int(hour) + 1
    if hour == 13:
      minute = 0
      hour = 1
      am_pm = am_pm + 1
      
      if am_pm == 3:
        am_pm = 1
      

    time.sleep(1)
    
    