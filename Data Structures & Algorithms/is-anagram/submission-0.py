class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for char in s:
            if char in d1.keys():
                d1[char] = d1[char] + 1
            else:
                d1[char] = 1
        for char in t:
            if char in d2.keys():
                d2[char] = d2[char] + 1
            else:
                d2[char] = 1
        return d1 == d2