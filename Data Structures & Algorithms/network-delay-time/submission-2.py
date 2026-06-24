class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for time in times:
            adjList[time[0]].append((time[1], time[2]))
        # print(adjList)
        seen = set()
        path = set()
        nodeMinTimes = {}
        def dfs(node, currTime):
            if node in path:
                return
            if currTime >= nodeMinTimes.get(node, float("inf")):
                return
            path.add(node)
            seen.add(node)
            nodeMinTimes[node] = min(nodeMinTimes.get(node, float("inf")), currTime)
            for dest, timeToAdd in adjList[node]:
                dfs(dest, currTime + timeToAdd)
            path.remove(node)
        dfs(k, 0)
        if len(seen) < n:
            return -1
        return max(nodeMinTimes.values())
