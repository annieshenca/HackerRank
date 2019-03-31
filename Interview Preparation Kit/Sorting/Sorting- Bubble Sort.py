#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    lengh = len(a)
    count = 0
    # Perform bubble sort
    # Within it, count number of swaps, then print first and last elements.
    for i in range(lengh):
        for j in range(lengh-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
    
    print ("Array is sorted in", count, "swaps.")
    print ("First Element:", a[0])
    print ("Last Element:", a[lengh-1])

if __name__ == '__main__':
    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)

