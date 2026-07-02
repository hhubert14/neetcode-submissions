class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def dfs(l, r):
            if l == r:
                return nums[l-1] * nums[l] * nums[r+1]
            if (l,r) in cache:
                return cache[(l,r)]
            maxAns = 0
            for i in range(l, r+1):
                maxAns = max(maxAns, nums[i] * nums[l-1] * nums[r+1] + dfs(l,i-1) + dfs(i+1,r))
            cache[(l,r)] = maxAns
            return maxAns
        return dfs(1,len(nums)-2)