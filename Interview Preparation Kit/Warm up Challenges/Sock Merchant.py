#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # Given an array of individual socks represented by numbers for different colors,
    # how many pairs of socks are there?

    dic = {}
    pair = 0
    # for ele in ar:
    #     if ele in dic:
    #         dic[ele] += 1
    #     else:
    #         dic[ele] = 1
    # for clr in dic:
    #     pair += (dic[clr]/2)

    # Loop through the array of socks
    for ele in ar:
        # Check if the dictionary already have a single sock waiting for its mate.
        if ele in dic:
            pair += 1
            del dic[ele] # delete the record in dict to start fresh for the color.
        # Add new entry if we have not seen this color sock before.
        else:
            dic[ele] = 1
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

