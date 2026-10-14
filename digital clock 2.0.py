import time

def clear():
    __import__('os').system('cls')
while True:
    clear()
    t = time.localtime()
    print(t.tm_hour - 12 if t.tm_hour > 12 else t.tm_hour, ":", f"{t.tm_min:02}:", f"{t.tm_sec:02}", "AM" if t.tm_hour < 12 else "PM")
    print(t.tm_mon,"/",t.tm_mday,"/",t.tm_year)
    time.sleep(1)