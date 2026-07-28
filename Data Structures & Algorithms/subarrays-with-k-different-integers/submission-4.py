class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        leftNear = 0
        leftFar = 0
        right = 0
        smallWindowCount = {}
        ans = 0
        while right < len(nums):
            smallWindowCount[nums[right]] = smallWindowCount.get(nums[right], 0) + 1
            while len(smallWindowCount) > k:
                smallWindowCount[nums[leftNear]] -= 1
                if smallWindowCount[nums[leftNear]] == 0:
                    del smallWindowCount[nums[leftNear]]
                leftNear += 1
                leftFar = leftNear
            while smallWindowCount[nums[leftNear]] > 1:
                smallWindowCount[nums[leftNear]] -= 1
                leftNear += 1

            if len(smallWindowCount) == k:
                ans += leftNear - leftFar + 1
            right += 1
        return ans
            
