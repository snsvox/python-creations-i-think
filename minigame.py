import time
import random
import os
from colorama import Fore,Back,Style,init

def clear():
    os.system('cls')
clear()

print("Red = r")
print("Green = g")
print("Yellow = y")
print("Blue = b")
print("type it in lowercase in the game")

init(autoreset=True)
input('Press "enter" when your ready por favor')

clear()

for i in range(4):
    if i == str(0):
        pass
    else:
        if i < 1:
            pass
        else:
            import winsound; winsound.Beep(900,250)
            if i == 1:
                print(Fore.GREEN + '3')
            elif i == 2:
                print(Fore.YELLOW + '2')
            elif i == 3:
                print(Fore.RED + '1')

    if i == 0:
        pass
    else:
        time.sleep(1)
        clear()
winstreak = 0

print(Fore.RED + 'GO!')
import winsound; winsound.Beep(1000,1000)
clear()

color_chooser = "r","g","y","b"
while True:
    level = 1
    for i in range(level):

        random1 = random.choice(color_chooser)

        winsound.Beep(900,250)
        time.sleep(0.5)
        if random1 == "r":
            print(Fore.RED + '▮')
        elif random1 == "g":
            print(Fore.GREEN + '▮')
        elif random1 == "y":
            print(Fore.YELLOW + '▮')
        elif random1 == "b":
            print(Fore.BLUE + '▮')

    time.sleep(0.15)
    clear()
    answer = input()
    if answer == random1:
        winsound.Beep(1250,250)
        time.sleep(0.25)
        print(Fore.GREEN + 'correct')
        winstreak += 1
        print("wintreak: ", winstreak)
        level += 1
    else:
        winsound.Beep(750,125)
        winsound.Beep(750,125)
        time.sleep(0.25)
        print(Fore.RED + 'incorrect')
        winstreak = 0
        level = 1
        print("wintreak: ", winstreak)
    for i in range(4):
        if i == str(0):
            pass
        else:
            print("continue in:", i)
            time.sleep(1)
    clear()
