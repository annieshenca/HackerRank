#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # The center of the hourglass will only go from one away from the start
    # to one away from the end. Therefore no need to check for surrounding
    # boundaries.
    max_sum = -100 # Minimum int that sum cannot pass. 
    for row in range(1, len(arr)-1):
        for col in range(1, len(arr[0])-1):
            # Now that we got the center number, start tracking the max sum.
            center = arr[row][col]
            top    = arr[row-1][col-1] + arr[row-1][col] + arr[row-1][col+1]
            bottom = arr[row+1][col-1] + arr[row+1][col] + arr[row+1][col+1]
            hourglass = center + top + bottom
            if hourglass > max_sum:
                max_sum = hourglass
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

