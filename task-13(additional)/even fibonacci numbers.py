#!/bin/python3

import sys

t = int(input())
q = []
for i in range(t):
    n = int(input())
    q.append(n)

def fib(n):
    p = []
    x, y = 1, 2
    c = 0
    if n == 1:
        print(x)
    else:
        while c < n:
            p.append(x)
            z = x + y
            x = y
            y = z
            c += 1
    return p


for i in q:
    m = 0
    for j in fib(i):
        if j % 2 == 0 and j <= i:
            m += j
    print(m)
