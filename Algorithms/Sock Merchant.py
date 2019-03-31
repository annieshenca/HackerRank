#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dic = {}
    pair = 0
    # for ele in ar:
    #     if ele in dic:
    #         dic[ele] += 1
    #     else:
    #         dic[ele] = 1
    # for clr in dic:
    #     pair += (dic[clr]/2)

    for ele in ar:
        if ele in dic:
            pair += 1
            del dic[ele]
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


