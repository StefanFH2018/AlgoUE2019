#!/usr/bin/python3

import time
import sys


def move(n, fromPeg = "A", toPeg = "B", withPeg = "C"):
    if n >= 1:
        move(n - 1, fromPeg, withPeg, toPeg)
        output_movement(fromPeg, toPeg)
        move(n - 1, withPeg, toPeg, fromPeg)


def output_movement(fp, tp):

    print("Move disk from",fp,"to",tp)
    output_movement.counter += 1

output_movement.counter = 0


orig_stdout = sys.stdout
f = open('StefanFH2018-TowersOfHanoi.out', 'w')
sys.stdout = f

for i in range(1,26):

    eingabe_n = i

    start = time.time()
    move(eingabe_n)
    end = time.time()

    print("Total number of disc move operations:", output_movement.counter)
    print("Runtime[s]:", (end - start))
    output_movement.counter = 0

sys.stdout = orig_stdout
f.close()




