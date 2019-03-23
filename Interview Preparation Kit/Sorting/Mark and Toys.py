#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    count = 0
    checkout = 0
    prices = sorted(prices) # Sorting the toy prices make this easier!
    for i in range(len(prices)):
        # if getting this new toy would have me still within budget,
        if checkout + prices[i] <= k:
            checkout += prices[i]
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = map(int, raw_input().rstrip().split())
    
    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

