"""
切棍子的最小成本
https://leetcode-cn.com/problems/minimum-cost-to-cut-a-stick/
"""


def gunzi(N, arr):
    dp = [[0]* (N +1) for i in range(N+1)]
    for i in range(N + 1):
        for j in range(i+1, N):
            tmp = 100000
            for k in range(i, j):
                if k not in arr:
                    continue
                tmp = min(tmp, dp[i][k] + dp[k][j])
            dp[i][j] = tmp + j - i
    print(dp)
    return dp[0][N-1]


N = 7
arr = [1,3,4,5]
result = gunzi(N, arr)
print(result)