#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    # 
    # 1. find LCM of a
    # 2. find GCD of b
    # 3. count the number of multiples of LCM that evenly divides the GCD
    # 
    
    # a_gcd = findGCD(a)
    # a_lcm = findLCM(a)
    # b_gcd = findGCD(b)
    # # b_lcm = findLCM(b)
    # count = 0
    # for i,j in range((a_lcm,2), b_gcd+1, (a_lcm*j, 1)):
    #     if b_gcd % i == 0:
    #         count += 1
    # print(i)
      
    nmax,nmin,count = max(a),min(b),0
    for i in range(1,int(nmin/nmax)+1):
        if(sum((i*nmax)%n for n in a)+sum(n%(i*nmax) for n in b))==0:
            count+=1
    return count
    
    
def singleGCD(x, y):
    while b != 0 and y != 0:
        x, y = y, x%y
    return x
    
def findGCD(l):
    result = l[0]
    for i in l:
        result = singleGCD(result, i)
    return result

def singleLCM(x, y):
    g = singleGCD(x, y)
    return (x * y)/g

def findLCM(l):
    result = l[0]
    for i in l:
        result = singleLCM(result, i)
    return result
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()


