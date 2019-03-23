#!/bin/python

import math
import os
import random
import re
import sys

# Determine the minimum number of jumps it will take Emma to jump from
# her starting postion to the last cloud represented by '0'.
# It is always possible to win the game.
# Each jump and only be 1 or 2 jumps from her current number. She must not step
# on thunderheads represented by '1'.

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    i = 0
    l = len(c)

    while i < l-1:
        # If the current position allow two jumps, then we jump 1 here.
        if (i+2 < l) and (c[i+2] == 0):
            i += 1
        # We can always be able to jump at least one.
        i += 1
        print (i)
        count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

