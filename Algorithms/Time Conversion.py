#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    parsed = s.split(":")
    if "PM" in parsed[2] and parsed[0] != "12":
        parsed[0] = int(parsed[0]) + 12
    if "AM" in parsed[2] and parsed[0] == "12":
        parsed[0] = "00"
    parsed[2] = parsed[2].replace("PM", "")
    parsed[2] = parsed[2].replace("AM", "")
    string = str(parsed[0]) +":"+ parsed[1] +":"+ str(parsed[2])
    return string
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()


