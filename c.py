n = int(input())


def calc(n, k):
    ans = 0
    rows = n // k
    rem = n % k
    for i in range(rows):
        for j in range(k):
            ans += (rows - i) * (k - j)
            if j < rem:
                ans += rem - j
    for i in range(rem):
        ans += rem - i
    return ans


minv = float('inf')
minn = -1
for i in range(1, n + 1):
    x = calc(n, i)
    if x < minv:
        minv = x
        minn = i
print(minn)
# mikushhhka
