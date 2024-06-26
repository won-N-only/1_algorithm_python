n = int(input())
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = int(input())

dp = [0] * (n + 1)
if n > 0:
    dp[1] = s[1]
if n > 1:
    dp[2] = s[1] + s[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i-1], dp[i-2] + s[i], dp[i-3] + s[i-1] + s[i])

print(dp[n])
