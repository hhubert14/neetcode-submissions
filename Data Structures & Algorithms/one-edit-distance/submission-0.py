class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        replace = True
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    if replace == True:
                        replace = False
                    else:
                        return False
            return True
        elif len(s) == len(t) - 1:
            l = 0
            while l < len(s) and s[l] == t[l]:
                l += 1
            r = len(s) - 1
            while r >= 0 and s[r] == t[r+1]:
                r -= 1
            if r < l:
                return True
            return False
        elif len(s) == len(t) + 1:
            l = 0
            while l < len(t) and s[l] == t[l]:
                l += 1
            r = len(t) - 1
            while r >= 0 and s[r+1] == t[r]:
                r -= 1
            if r < l:
                return True
            return False
        return False

