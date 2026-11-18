class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * (length + 1)
        for update in updates:
            ans[update[0]] += update[2]
            ans[update[1] + 1] -= update[2]
        
        curr = 0
        # print(ans)
        for i in range(len(ans)):
            curr += ans[i]
            ans[i] = curr
        return ans[:-1]
