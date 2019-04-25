#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    # Use the Counter function to easily do the letter count.
    c = Counter(s)
    # Turn the counts into a sorted list
    vals = list(c.values())
    vals.sort()

    l = len(vals)
    min_val = vals[0]
    max_val = vals[l-1]
    
    if vals.count(max_val) > 1 or max_val-min_val > 1:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

