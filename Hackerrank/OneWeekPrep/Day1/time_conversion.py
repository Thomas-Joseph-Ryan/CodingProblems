#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s : str):
    # Write your code here
    if s.endswith("AM"):
        return convertAM(s.strip("AM"))
    else:
        return convertPM(s.strip("PM"))

def convertAM(s : str):
    if s.startswith("12"):
        s = "00" + s.split("12")[1]
    return s
        

def convertPM(s: str):
    if s.startswith("12"):
        return s
    s = s.split(":")
    hour = int(s[0])
    hour = hour + 12
    s[0] = str(hour)
    return ':'.join(s)
        
if __name__ == '__main__':
    print(timeConversion("03:01:00PM"))
