class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i, j):
            nonlocal s
            nonlocal p
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(p):
                return i == len(s)

            res = False
            if j+1 < len(p) and p[j+1] == "*":
                res = dfs(i, j+1)
            elif i < len(s) and (s[i] == p[j] or p[j] == "."):
                res = dfs(i+1, j+1)
            if p[j] == "*":
                if i < len(s) and (s[i] == p[j-1] or p[j-1] == "."):
                    res = dfs(i+1, j) or dfs(i+1, j+1)
                res = res or dfs(i, j+1) 
            cache[(i,j)] = res
            return cache[(i,j)]
        return dfs(0, 0)