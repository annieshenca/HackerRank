#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    # Since we don't have to return the modified string, all we need to focus
    # on is the counter.
    # Loop through the string and increment counter.
    counter = 0
    for i in range( len(s)-1 ):
        # Check if current letter is the same as the next, if so, this 
        # increases the counter.
        if s[i] == s[i+1]:
            counter += 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

