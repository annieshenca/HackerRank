#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # Create hash table for both magazines, then check if M has what N needs in terms
    # of both letters and letter counts.
    mdict = {}
    ndict = {}
    same = "Yes"
    for m in magazine:
        mdict[m] = 1 if m not in mdict else mdict[m]+1
    for n in note:
        ndict[n] = 1 if n not in ndict else ndict[n]+1
    for word in ndict:
        if word not in mdict or ndict[word] > mdict[word]:
            same = "No"
    print same

if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
