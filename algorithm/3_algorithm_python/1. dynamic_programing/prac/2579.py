n = int(input())
s = [0] * (n + 1)

for i in range(1, n + 1):
    s[i] = int(input())

d = [[0]*3 for _ in range(n + 1)]

if n == 1:
    print(s[1])
else:
    d[1][1] = s[1]
    d[1][2] = 0
    d[2][1] = s[2]
    d[2][2] = s[1] + s[2]

    for i in range(3, n + 1):
        d[i][1] = max(d[i-2][1], d[i-2][2]) + s[i]
        d[i][2] = d[i-1][1] + s[i]

    print("\n", max(d[n][1], d[n][2]))
