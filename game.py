#! /usr/bin/env python3
"""
# For best results use source code pro
# Arrows
# "←..↑..↓..→"
"""

import datetime
import random
import getpass
#Stupid windows # <- I agree...
try:
    import msvcrt
except ImportError:
    import getch
    msvcrt = getch
import time
import sys


try:
    MODE = sys.argv
except IndexError:
    MODE = 'default'

class GameEnv(): # pylint: disable=too-many-instance-attributes, too-few-public-methods
    """
    Start up variables
    """
    score = 0
    accu = 0
    hearts = 3
    streak = 0
    long_streak = 0
    fallback = False
    giant = False
    g = False
    gtr = False
    gtro = False

GAME_SETTINGS = GameEnv()

def game():
    """
    Game logic
    """
    if 'help' in MODE:
        print("Usage: ./game.py [ fallback | giant ] [ g ] ")
        print("See README for more details.")
        sys.exit()

    total = 0
    if 'g' in MODE:
        GAME_SETTINGS.g = True # pylint: disable=invalid-name
        GAME_SETTINGS.hearts = 0
    if 'fallback' in MODE:
        GAME_SETTINGS.fallback = True
    elif 'giant' in MODE:
        GAME_SETTINGS.giant = True
    elif 'gtr' in MODE:
        GAME_SETTINGS.gtr = True
    elif 'gtro' in MODE:
        GAME_SETTINGS.gtro = True

    heart = " ❤"
    start = time.time()
    while True:
        direction = random.choice(['h', 'j', 'k', 'l'])
        ddr(direction, GAME_SETTINGS.hearts, heart)
        char = msvcrt.getch().lower()
        total = total + 1
        if char == 'q':
            break
        elif char != direction:
            GAME_SETTINGS.long_streak = max(GAME_SETTINGS.streak, GAME_SETTINGS.long_streak)
            GAME_SETTINGS.streak = 0
            GAME_SETTINGS.hearts = GAME_SETTINGS.hearts - 1
            if GAME_SETTINGS.hearts == 0:
                break
        else:
            GAME_SETTINGS.streak = GAME_SETTINGS.streak + 1
            GAME_SETTINGS.score = GAME_SETTINGS.score + 1

    end = time.time()
    time_completion = round(end - start, 2)
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = getpass.getuser()
    GAME_SETTINGS.accu = str(round(GAME_SETTINGS.score * 100/total, 2))+ '%'
    record_scores(user, date, GAME_SETTINGS.accu, GAME_SETTINGS.score, GAME_SETTINGS.long_streak)
    print("Time : ", str(time_completion)+"s")
    print("Accu : ", GAME_SETTINGS.accu, "(", GAME_SETTINGS.score, "of", total, ")")
    print("Speed: ", round(GAME_SETTINGS.score/time_completion, 2), "strokes/sec")
    print("Longest streak: ", GAME_SETTINGS.long_streak)

def record_scores(user, date, accu, score, long_streak):
    """
    Score is recorded to scores.txt
    """
    outstr = "\t".join([user, str(score), accu, str(long_streak), str(time) + "s\t", date])
    with open("scores.txt", "a") as score_file:
        score_file.write(outstr + "\n")

def gethearts(num, heart):
    """
    Hearts are managed here
    """
    heart_count = ""
    while num > 0:
        heart_count = heart_count + heart
        num = num - 1
    return heart_count

def ddr(dirn, hearts, heart):
    """
    DDR is printed here
    """
    left = "←         "
    down = "   ↓      "
    up_up = "      ↑   "
    right = "         →"
    heart = " ❤"

    if GAME_SETTINGS.fallback:
        left = "<           "
        down = "   v        "
        up_up = "      ^     "
        right = "         >  "
        heart = " <3"

    if GAME_SETTINGS.giant:
        left = "  /\n /\n \\\n  \\                      "
        down = "    \\      /\n     \\    /\n      \\  /\n       \\/                "
        up_up = "                /\\\n               /  \\\n              /    \\\n             /      \\    "
        right = "                      \\\n                       \\\n                       /\n                      /  "
        heart = "<3 "

    if GAME_SETTINGS.gtr:
        left = "\033[1;31;49mH\033[1;30m  |  |  |  "
        down = "|  \033[1;32;49mJ\033[1;30m  |  |  "
        up_up = "|  |  \033[1;33;49mK\033[1;30m  |  "
        right = "|  |  |  \033[1;34;49mL\033[1;30m  "
        heart = " <3"


    if GAME_SETTINGS.gtro:
        left = "\033[1;31;49mO\033[1;30m  |  |  |  "
        down = "|  \033[1;32;49mO\033[1;30m  |  |  "
        up_up = "|  |  \033[1;33;49mO\033[1;30m  |  "
        right = "|  |  |  \033[1;34;49mO\033[1;30m  "
        heart = " <3"


    if dirn == 'h':
        print(left+ gethearts(hearts, heart))
    elif dirn == 'j':
        print(down+ gethearts(hearts, heart))
    elif dirn == 'k':
        print(up_up + gethearts(hearts, heart))
    elif dirn == 'l':
        print(right + gethearts(hearts, heart))



if __name__ == "__main__":
    game()
