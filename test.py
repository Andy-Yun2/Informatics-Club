n = int(input())
a_cost = int(input())
b_cost = int(input())

dp = [float('inf')] * (n + 1)

dp[0] = 0

for i in range(1, n + 1):
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + a_cost)

    if i >= 3:
        dp[i] = min(dp[i], dp[i - 3] + b_cost)

if dp[n] != float('inf'):
    print(dp[n])