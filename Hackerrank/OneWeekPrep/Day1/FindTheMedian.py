#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr :list[int]):
    arr.sort()
    middle_index = len(arr) // 2
    return arr[middle_index]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    # result = findMedian(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(findMedian([5, 3, 1, 2, 4]))
