class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = [[False] * len(grid[0]) for _ in range(len(grid))]
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append([row, col, 0])
        while queue:
            row, col, minDist = queue.popleft()
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])) or seen[row][col] or grid[row][col] == -1:
                continue
            seen[row][col] = True
            grid[row][col] = minDist
            queue.append([row+1,col,minDist+1])
            queue.append([row-1,col,minDist+1])
            queue.append([row,col+1,minDist+1])
            queue.append([row,col-1,minDist+1])
            