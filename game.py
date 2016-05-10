#! /usr/bin/python3
# -*- coding: utf-8 -*-

# For best results use source code proj
# TODO: use a prettifier like toilet/figlet
# Arrows
# "←..↑..↓..→"

import random
import getch
import time

score = 0

fallback = False

left  = "←         "
up    = "   ↓      "
down  = "      ↑   "
right = "         →"

if fallback:
    left  = "<         "
    up    = "   v      "
    down  = "      ^   "
    right = "         >"

start = time.time()
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
end = time.time()
time = round(end - start, 2)
print("Time : ", time)
print("Score: ", score)
print("Speed: ", round(score/time,2))
