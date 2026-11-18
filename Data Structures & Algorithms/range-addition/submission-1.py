class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * (length + 1)
        for update in updates:
            ans[update[0]] += update[2]
            if update[1] + 1 < length:
                ans[update[1] + 1] -= update[2]
        
        for i in range(1, len(ans)):
            ans[i] += ans[i-1]
        return ans[:-1]
