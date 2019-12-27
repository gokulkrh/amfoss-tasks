#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    m = n-2
    for i in range(1,n):
        print(' ' * m, '#' * i)
        m -= 1
    x = print('#' * n)
    return x
if __name__ == '__main__':
    n = int(input())

    staircase(n)

