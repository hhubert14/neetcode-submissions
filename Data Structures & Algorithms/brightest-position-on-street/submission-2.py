class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        changes = defaultdict(int)
        for light in lights:
            changes[light[0] - light[1]] += 1
            changes[light[0] + light[1] + 1] -= 1
            
        curr = 0
        ansVal = 0
        ansIdx = -1
        for i in sorted(changes):
            curr += changes[i]
            if curr > ansVal:
                ansVal = curr
                ansIdx = i
        
        return ansIdx