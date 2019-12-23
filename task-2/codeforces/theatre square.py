n, m, a = map(int, input().split())
t = n * m
f = a ** 2
c = 0
while m > 0:
    c += 2
    m -= a
w = a * 2
while n > w:
    c += 2
    n -= w
u = c * f
while t > u:
    c += 1
    t -= w
print(c)