import keyboard
import os
import random
import math
from time import sleep

import pyfiglet
from rich.console import Console

import hackertype


def show_header(con):
    banner = pyfiglet.figlet_format("DARKWEB", font="banner3-D")
    con.print(banner, "Penetrating server firewall in...", style="bold green")
    for i in range(0, 4):
        sleep(1)
        if(i == 3):
            print("                          ", end="\r")
        else:
            print(str(3-i) + "...", end='\r')


def updatebar(con):
    bar = "|"+" "*10 + "|"
    progress = 0
    loading_bar_char = "█"

    while True:
        if(progress > 10):
            print("                          ", end="\r")
            con.print("SUCCESSFUL", style="bold green")
            break
        else:
            sleep(0.3)
            increment = random.random()
            if math.floor(progress) < math.floor(progress + increment):
                bar = "[" + math.floor(progress+increment) * loading_bar_char + \
                    (10-math.floor(progress+increment)) * "_" + "]"
            progress += increment
            print("{:.2f}".format(min((progress*10), 100)
                                  ) + "%" + bar + str("{:.2f}".format(increment)) + "/s", end='\r', flush=True)


def penetrate():
    con = Console()
    show_header(con)
    updatebar(con)
    con.print(
        "Admin privileges acquired... Ready to implant virus code", style="bold red")
    hackertype.hackertype('python')
    print("\n")
    con.print("\nLogged Out... Successfully implanted", style="bold green")
    sleep(1)


if __name__ == '__main__':
    penetrate()
