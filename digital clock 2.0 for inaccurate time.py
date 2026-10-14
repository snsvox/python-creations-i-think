#pls dont change anything all is gud rn :)

import time
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

while True:
    t = time.localtime()
    h = t.tm_hour - 7

    clear()
    print(h - 12 if h > 12 else h,":",f"{t.tm_min:02}",":",f"{t.tm_sec:02}","AM" if t.tm_hour < 12 else "PM")
    print(t.tm_mon,"/",t.tm_mday,"/",t.tm_year)
    time.sleep(1)
        