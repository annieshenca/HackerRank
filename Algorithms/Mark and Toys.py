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
    prices = sorted(prices)
    for i in range(len(prices)):
        # if getting this new toy would have me still within budget,
        if checkout+prices[i] <= k:
            checkout += prices[i]
            count += 1
    return count
'''
// Complete the maximumToys function below.
static int maximumToys(int[] prices, int k, int current ) {
    if(current == prices.length) return 0; // ran out of items
    if(k < 0) return  0; // spent too much
    if(k == 0) return 1; // out of money
    // afford item?
    int item = 1;
    if(k < prices[current])  {
        item = 0;
    }
    // max of either adding the item (assuming you can afford it or not).
    return Math.max(item + maximumToys(prices, k-prices[current], current+1),  
        maximumToys(prices,k, current+1));
} 
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = map(int, raw_input().rstrip().split())
    
    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()


