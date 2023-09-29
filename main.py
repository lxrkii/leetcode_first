class Solution(object):
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        return dp[len(s)][len(p)]
solution = Solution()
s1 = "aa"
p1 = "a"
print(solution.isMatch(s1, p1))
s2 = "aa"
p2 = "a*"
print(solution.isMatch(s2, p2))
s3 = "ab"
p3 = ".*"
print(solution.isMatch(s3, p3))