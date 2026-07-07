class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def getSum(num):
            ans = 0
            while num:
                ans += (num % 10) ** 2
                num //= 10
            return ans
        while n != 1:
            n = getSum(n)
            if n in seen:
                return False
            seen.add(n)
        return True