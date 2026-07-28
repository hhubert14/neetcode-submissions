class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        leftNear = 0
        leftFar = 0
        right = 0
        smallWindowCount = {}
        ans = 0
        while right < len(nums):
            # print("-----------")
            # print(f"{leftFar=}")
            # print(f"{leftNear=}")
            # print(f"{right=}")
            # print(f"{largeWindowCount=} before")
            # print(f"{smallWindowCount=} before")
            smallWindowCount[nums[right]] = smallWindowCount.get(nums[right], 0) + 1
            if len(smallWindowCount) > k:
                while len(smallWindowCount) > k:
                    smallWindowCount[nums[leftNear]] -= 1
                    if smallWindowCount[nums[leftNear]] == 0:
                        del smallWindowCount[nums[leftNear]]
                    leftNear += 1
                leftFar = leftNear
            # else:
            while smallWindowCount[nums[leftNear]] > 1:
                smallWindowCount[nums[leftNear]] -= 1
                leftNear += 1

            if len(smallWindowCount) == k:
                ans += leftNear - leftFar + 1
            right += 1
            # print(f"{largeWindowCount=} after")
            # print(f"{smallWindowCount=} after")
            # print(f"{ans=}")
        return ans
            
