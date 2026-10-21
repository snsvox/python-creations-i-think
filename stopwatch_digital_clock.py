import time
import os
import math
import threading
from colorama import Fore,Back,Style,init
import sys

init(autoreset=True)

starter = 0
stopper = 0
thread_stopper = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

print("this is a uh something")

while True:
    t1 = time.localtime()
    print(f"day: {t1.tm_mon} / {t1.tm_mday} / {t1.tm_year}"'\n')

    print("1 - digital clock")
    print("2 - stopwatch"'\n')
    print(f"if you are using the digital clock press {Fore.RED + "enter"} {Fore.LIGHTWHITE_EX + "two times to go back here"}")
    choice = input("if u are using the stopwatch press enter to stop it ")

    clear()

    if choice == "1":
        stopper = 0
        def backround_task():
            while True:
                if stopper == '':
                    clear()
                    break
                else:
                    pass

                t = time.localtime()
                h = t.tm_hour - 7

                print(h - 12 if h > 12 else h,":",f"{t.tm_min:02}",":",f"{t.tm_sec:02}","AM" if t.tm_hour < 12 else "PM")
                print(t.tm_mon,"/",t.tm_mday,"/",t.tm_year)

                time.sleep(1)
                clear()

        thread = threading.Thread(target=backround_task)
        thread.start()
        stopper = input()
        
    elif choice == "2":
        input("press enter to start the stopwatch")
        start_time = time.time()
        input("press enter to stop the stopwatch")
        stop_time = time.time()
        elapsed = start_time - stop_time
        res = elapsed - elapsed
        result = res - elapsed
        print(f"elapsed time: {round(result,2)}")
        input("press 'enter' to continue")

    clear()
