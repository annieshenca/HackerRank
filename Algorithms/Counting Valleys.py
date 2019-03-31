#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sealevel = 0
    cur = 0         # Current altertude. Start at sealevel
    count = 0

    for step in s:
        if step == "U":
            cur += 1
            if cur == sealevel:
                count += 1
        else:
            cur -= 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


