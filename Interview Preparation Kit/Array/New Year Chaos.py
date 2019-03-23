#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps = 0
    for i in range(len(q)-1, -1, -1):
        # If we find that the value at specific index is 2 more than the value, then
        # this has broken the rules. Return "Too chaotic"
        if q[i]-(i+1) > 2:
            print ("Too chaotic")
            return
        
        # Now we check how many swaps happened by looking through the indexes behind i.
        for j in range( max(0, q[i]-2), i ):
            if q[j] > q[i]:
                # No need to swap the values' position since we're only counting here.
                swaps += 1
    print swaps

    ## Below code ideas did not work at all ;D
    # counter = 0
    # # One for loop start from back of the array
    # for idx in range(len(q)-1, -1, -1):
    #     # Comparing if q[i] is the same as i
    #     if idx != q[idx]:
    #         # If do not equal, then this means the original element has
    #         # tried to bribe forward. Now check if it's within one or
    #         # two steps forward.
    #         if q[idx-1] == q[idx]:
    #             # Swap and increment counter by 1
    #             q[idx-1], q[idx] = q[idx], q[idx-1]
    #             counter += 1
    #         elif q[idx-2] == q[idx]:
    #             q[idx-2], q[idx] = q[idx], q[idx-2]
    #             counter += 1
    #         else:
    #             # Either out of range, or the element moved too far.
    #             print "Too chaotic"
    # # print counter 

    # swaps = 0
    # swaped = False
    # # First check if the queue is already "Too chaotic".
    # for idx, ele in enumerate(q):
    #     # ele-1 -> to match idx started with 0.
    #     if (ele-1) - idx > 2:
    #         print "Too chaotic"
    #         return
    # # Use Bubble Sort to count swaps.
    # for i in xrange(0, len(q)):
    #     # The diff between range() and xrange() is that x is better for
    #     # memory restricted sys. Range() is better for going over many times.
    #     for j in xrange(0, len(q)):
    #         if q[j] > q[j+1]:
    #             q[j], q[j+1] = q[j+1], q[j]
    #             swaps += 1
    #             swaped = True
    #     if swaped:  swaped = False
    #     else:       break
    # print swaps


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
