#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.

def stepPerms1(n):
    # Create tuples of f1, f2, and f3 to represent the number of ways to climb
    # stairs of height 1, 2, and 3.
    # Stairs of height 3 equals to 4 because there's 4 ways to climb stairs of height 3.
    f1, f2, f3 = 1, 2, 4
    for i in range(n-1):
        f1, f2, f3 = f2, f3, f1+f2+f3
    return f1

# Use memoization to store the value for when the stair heights are 1, 2, and 3.
def stepPerms2(n):
    memo = dict()
    memo[0] = 1
    memo[1] = 2
    memo[2] = 4
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms1(n)
        # res = stepPerms2(n)

        fptr.write(str(res) + '\n')

    fptr.close()
