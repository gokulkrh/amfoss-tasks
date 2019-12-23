n, k = map(int, input().split())
x = list(map(int, input().split()))[:n]
c = 0
o = x[k-1]
for i in x:
    if i >= o and i != 0:
        c += 1
if c >0 :
    print(c)
else:
    print('0')