class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            currChar = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != currChar:
                    return ans
            ans += currChar
        return ans