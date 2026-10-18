class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        currPos = 0
        while currPos < len(nums) and nums[currPos] != 0:
            currPos += 1
        i = currPos + 1
        while i < len(nums):
            if nums[i] != 0:
                nums[currPos], nums[i] = nums[i], nums[currPos]
                currPos += 1
            i += 1