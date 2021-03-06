#!/bin/python

import math
import os
import random
import re
import sys

# Given an integer, , find and print the number of
# letter a's in the first  letters of Lilah's infinite string.

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    k = n/l
    f = n%l
    count = 0

    for i in s:
        if i == 'a':
            count += 1
    
    a = count * k
    
    for i in range(0, f):
        if s[i] == 'a':
            a += 1

    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

