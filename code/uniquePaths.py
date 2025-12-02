class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                prev[j] += prev[j - 1]
        return prev[-1]