#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # The the Counter function to map out the [letter: count]
    a_counter = Counter(a)
    b_counter = Counter(b)

    # Have the a_counter minus b_counter. Now we're left with
    # everything that did NOT have in common.
    a_counter.subtract(b_counter)
    print(a_counter)
    
    # Add up the count of the left over letters.
    return sum(abs(i) for i in a_counter.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

