#!/bin/python

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(money, n, cost):
    result = {}
    for i in range(n):
        # If the price of flavor we are on right now is already in
        # the hashtable, meaning we've added the first flavor and 
        # looking for the fitting second to spend all the money,
        # then mark that down, and break out of loop to return the
        # final flavor result
        if cost[i] in result:
            print result[cost[i]], i+1
            break
        # Make the dict key to be the amount we are now looking for
        # for the second flavor, the value of the key is the index
        # of that flavor you're adding into the hashtable 
        result[money - cost[i]] = i + 1

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        money = int(raw_input())

        n = int(raw_input())

        cost = map(int, raw_input().rstrip().split())

        whatFlavors(money, n, cost)

