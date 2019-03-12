#!/usr/bin/python3

import time
import sys
from argparse import ArgumentParser


def move(n, fromPeg = "A", toPeg = "B", withPeg = "C"):
    if n >= 1:
        move(n - 1, fromPeg, withPeg, toPeg)
        output_movement(fromPeg, toPeg)
        move(n - 1, withPeg, toPeg, fromPeg)


def output_movement(fp, tp):

    print("Move disk from",fp,"to",tp)
    output_movement.counter += 1

output_movement.counter = 0

parser = ArgumentParser()
parser.add_argument('-n', '--numbers',type = int, help = 'geben Sie die gewünschte Anzahl der Scheiben des Puzzles an')

args = parser.parse_args()

eingabe_n: object = int(args.numbers)


start = time.time()

move(eingabe_n)

end = time.time()


print("Total number of disc move operations:",output_movement.counter,file=sys.stderr)
print("Runtime[s]:",(end - start),file=sys.stderr)


