n = int(input())
w = []
for i in range(n):
    s = input()
    w.append(s)
for i in w:
    i = list(i)
    if len(i) > 10:
        b = list(i)
        b.pop(0)
        b.pop(len(b) - 1)
        c = [i[0], len(b), i[len(i) - 1]]
        q = ""
        for j in c:
            j = str(j)
            q += j
        print(q)
    else:
        q = ""
        for j in i:
            q += j
        print(q)