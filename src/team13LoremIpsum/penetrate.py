import keyboard
import os
import random
import math
from time import sleep

import pyfiglet
from rich.console import Console

import hackertype

# Global Var
con = Console()
bar = "|"+" "*10 + "|"
progress = 0
loading_bar_char = "█"


def show_header():
    banner = pyfiglet.figlet_format("DARKWEB", font="banner3-D")
    con.print(banner, "Penetrating server firewall in...", style="bold green")
    for i in range(0, 4):
        sleep(1)
        if(i == 3):
            print("                          ", end="\r")
        else:
            print(str(3-i) + "...", end='\r')


def updatebar_by_input(increment_base=0.1):
    global progress
    global bar

    if(progress > 10):
        os.system('cls')
        print("SUCCESSFUL")

    else:
        increment = random.random() * increment_base
        if math.floor(progress) < math.floor(progress + increment):
            bar = "|" + math.floor(progress+increment) * loading_bar_char + \
                (10-math.floor(progress+increment)) * "_" + "|"
        progress += increment
        # os.system('cls')
        print(bar + "{:.2f}".format(progress*10) + "%", end='\r', flush=True)


def updatebar():
    global progress
    global bar
    global con
    if(progress > 10):
        print("                          ", end="\r")
        con.print("SUCCESSFUL", style="bold green")
        return False
    else:
        sleep(0.3)
        increment = random.random()
        if math.floor(progress) < math.floor(progress + increment):
            bar = "[" + math.floor(progress+increment) * loading_bar_char + \
                (10-math.floor(progress+increment)) * "_" + "]"
        progress += increment
        print("{:.2f}".format(min((progress*10), 100)
                              ) + "%" + bar + str("{:.2f}".format(increment)) + "/s", end='\r', flush=True)

        return True


def penetrate():
    # keyboard.on_press(lambda e: updatebar_by_input())
    # keyboard.wait('esc')
    show_header()
    while(updatebar()):
        pass
    con.print(
        "Admin privileges acquired... Ready to implant virus", style="bold red")
    hackertype.hackertype('python')
    print("\n")
    con.print("\nLogged Out... Successfully implanted", style="bold green")
    sleep(1)


penetrate()
