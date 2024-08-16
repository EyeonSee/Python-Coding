#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(n, arr):
    positive = 0
    negative = 0
    zero = 0
    for i in range(n):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero += 1
    print("{:.6f}".format(positive/n))
    print("{:.6f}".format(negative/n))
    print("{:.6f}".format(zero/n))

n = int(input())
arr = list(map(int, input().split()))
plusMinus(n, arr)