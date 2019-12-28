#!/bin/python3

import sys


t = int(input())
q = []
for i in range(t):
    n = int(input())
    q.append(n)


def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


for i in q:
    p = []
    for k in range(1,i+1):
        if i%k == 0:
            p.append(k)
    u = []
    for o in p:
        if prime(o):
            u.append(o)
    print(max(u))