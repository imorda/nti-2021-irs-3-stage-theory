T, C, W = map(int, input().strip().split())
n = int(input().strip())

ans = []
for i in range(n):
    name = ''
    kw = 0
    temp = 0
    flag = -1
    string = input().strip()
    for id, i in enumerate(string):
        if flag < 0:
            if i.isalpha() or i == ' ':
                name += i
            else:
                flag = id
                break
    name.strip()
    kw, temp = map(int, string[flag:].split())


    cost = 0
    if temp > T:
        cost = ((temp - T) * C) * kw
    elif temp < T:
        cost = ((T - temp) * W) * kw
    ans.append((cost, name))
ans.sort()

for i in ans:
    print(i[1], i[0], sep='')
