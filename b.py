n = int(input())
str_orig = input().strip()

ans = []
counter = 0
for id, i in enumerate(str_orig):
    if i == 'A':
        counter += 2**id
ans.append(counter)

counter = 0
for id, i in enumerate(str_orig):
    if i == 'B':
        counter += 2**id
ans.append(counter)

ans.sort()
for i in ans:
    print(i, end=' ')
