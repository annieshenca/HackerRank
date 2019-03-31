#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lowest = scores[0]
    passLowestCount = 0
    highest = scores[0]
    passHighestCount = 0

    for n in scores:
        if n < lowest:
            lowest = n
            passLowestCount += 1
        if n > highest:
            highest = n
            passHighestCount += 1
    
    return passHighestCount, passLowestCount



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


