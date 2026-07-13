class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                res = dfs(i+1, j+1)
            else:
                res = 1 + min(dfs(i+1, j+1), dfs(i, j+1), dfs(i+1, j))
            
            memo[(i, j)] = res
            return res

        return dfs(0,0)