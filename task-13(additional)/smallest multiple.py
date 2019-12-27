#!/bin/python3

import sys
from math import gcd


t = int(input().strip())
q = []
for i in range(t):
    n = int(input().strip())
    q.append(n)
for i in q:
    a = []
    for j in range(1,i+1):
        a.append(j)
    lcm = a[0]
    for e in a[1:]:
        lcm = lcm*e//gcd(lcm, e)
    print(lcm)
