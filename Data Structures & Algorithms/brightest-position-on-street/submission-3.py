class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        changes = defaultdict(int)
        for light in lights:
            changes[light[0] - light[1]] += 1
            changes[light[0] + light[1] + 1] -= 1
        
        ansVal = 0
        ansIdx = float("-inf")
        currBrightness = 0
        for key in sorted(changes):
            currBrightness += changes[key]
            if currBrightness > ansVal:
                ansIdx = key
                ansVal = currBrightness
        return ansIdx