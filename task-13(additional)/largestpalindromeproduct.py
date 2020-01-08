#!/bin/python3

import sys


t = int(input())
q = []
for i in range(t):
    n = int(input())
    q.append(n)

for c in q:
    x = 100
    p = []
    while x < 1000:
        for i in range(1000, 100, -1):
            for j in range(1000, 100, -1):
                prod = str(i * j)
                if prod == prod[::-1] and int(prod) < c:
                    p.append(int(prod))
                    break
                x = x + 1
        print(max(p))
