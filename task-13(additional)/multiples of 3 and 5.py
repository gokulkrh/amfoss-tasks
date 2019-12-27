#!/bin/python3

import sys


def sum(n, k):
    d = n // k
    return k * (d * (d + 1)) // 2


def func(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(func(n - 1))
