#! /usr/bin/python3
# -*- coding: utf-8 -*-

# For best results use source code proj
# TODO: use a prettifier like toilet/figlet
# Arrows
# "←..↑..↓..→"

import random
import getch

score = 0

left  = "←         "
up    = "   ↓      "
down  = "      ↑   "
right = "         →"

def ddr(dirn):
    if dirn == 'h':
        print(left)
    elif dirn == 'j':
        print(up)
    elif dirn == 'k':
        print(down)
    elif dirn == 'l':
        print(right)

while True:
    direction = random.choice(['h','j','k','l'])
    ddr(direction)
    char = getch.getch()
    if char != direction:
        break
    score = score + 1

print("Score: ", score)
