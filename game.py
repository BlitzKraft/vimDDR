#! /usr/bin/env python3

# For best results use source code pro
# Arrows
# "←..↑..↓..→"

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

score = 0
accu = 0
hearts = 3
fallback = False
giant = False
inf = False

try:
    mode = sys.argv
except IndexError:
    mode = 'default'

if 'help' in mode:
    print("Usage: ./game.py [ fallback | giant ] [ inf ] ")
    print("See README for more details.")
    sys.exit()

total = 0
if 'inf' in mode:
    inf = True
    hearts = 0
if 'fallback' in mode:
    fallback = True
elif 'giant' in mode:
    giant = True

left  = "←         "
down  = "   ↓      "
up    = "      ↑   "
right = "         →"
heart = " ❤"

if fallback:
    left  = "<           "
    down  = "   v        "
    up    = "      ^     "
    right = "         >  "
    heart = " <3"

if giant:
    left  = "  /\n /\n \\\n  \\                      "
    down  = "    \\      /\n     \\    /\n      \\  /\n       \\/                "
    up    = "                /\\\n               /  \\\n              /    \\\n             /      \\    "
    right = "                      \\\n                       \\\n                       /\n                      /  "
    heart = "<3 "

start = time.time()
def ddr(dirn):
    if dirn == 'h':
        print(left + gethearts(hearts))
    elif dirn == 'j':
        print(down + gethearts(hearts))
    elif dirn == 'k':
        print(up + gethearts(hearts))
    elif dirn == 'l':
        print(right + gethearts(hearts))

def gethearts(num):
    hc = ""
    while num > 0:
        hc = hc + heart
        num = num - 1
    return hc

def main():
    while True:
        direction = random.choice(['h','j','k','l'])
        ddr(direction)
        char = msvcrt.getch().lower()
        #if inf:
        global total
        total = total + 1
        if char == 'q':
            break
        elif char != direction:
            global hearts
            hearts = hearts - 1
            if hearts == 0:
                break
        else:
            global score
            score = score + 1
main()

def record_scores():
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = getpass.getuser()
    global accu
    accu = str(round(score * 100/total, 2))+ '%'
    outstr = "\t".join([user, str(score), accu, str(time) + "s\t", date])
    with open("scores.txt", "a") as score_file:
        score_file.write(outstr + "\n")

end = time.time()
time = round(end - start, 2)
record_scores()
print("Time : ", str(time)+"s")
print("Accu : ", accu, "(", score, "of", total, ")")
print("Speed: ", round(score/time,2), "strokes/sec")

