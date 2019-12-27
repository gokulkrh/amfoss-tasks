#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

n = int(input())
r = 0
l = 0
for i in range(n):
    a = list(map(int, input().split()))[:n]
    r += a[i]
    b = a[::-1]
    l += b[i]
print(abs(r-l))