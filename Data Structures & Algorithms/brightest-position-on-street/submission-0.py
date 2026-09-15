class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        diff = defaultdict(int)
        for light in lights:
            start, end = light[0] - light[1], light[0] + light[1]
            diff[start] += 1
            diff[end + 1] -= 1
        ansCount = 0
        ansIdx = 0
        currCount = 0
        for key in sorted(diff):
            currCount += diff[key]
            if currCount > ansCount:
                ansCount = currCount
                ansIdx = key
        return ansIdx