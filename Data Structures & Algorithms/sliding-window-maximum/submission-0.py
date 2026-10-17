class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        maxHeap = []
        l = 0
        r = k
        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
            count[nums[i]] += 1
        ans = []
        while r < len(nums):
            while -maxHeap[0] not in count:
                heapq.heappop(maxHeap)
            ans.append(-maxHeap[0])
            heapq.heappush(maxHeap, -nums[r])
            count[nums[r]] += 1
            count[nums[l]] -= 1
            if count[nums[l]] == 0:
                del count[nums[l]]
            l += 1
            r += 1
        while -maxHeap[0] not in count:
            heapq.heappop(maxHeap)
        ans.append(-maxHeap[0])
        return ans