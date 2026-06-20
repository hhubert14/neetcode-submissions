class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        for edge in edges:
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            adjList[edge[0]].append(edge[1])
            if edge[1] not in adjList:
                adjList[edge[1]] = []
            adjList[edge[1]].append(edge[0])
        seen = set()
        def dfs(currNode):
            if currNode in seen:
                return
            seen.add(currNode)
            for neighbor in adjList[currNode]:
                dfs(neighbor)
        ans = 0
        for key in adjList.keys():
            if key not in seen:
                ans += 1
            dfs(key)
        ans += n - len(seen)
        return ans