class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        ROWS = len(grid)
        COLS = len(grid[0])

        n_islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    queue = deque([[r, c]])
                    n_islands += 1
                    while queue:
                        nr, nc = queue.popleft()
                        for dr, dc in directions:
                            nr2, nc2 = nr + dr, nc + dc
                            if 0 <= nr2 < ROWS and 0 <= nc2 < COLS and grid[nr2][nc2] == "1":
                                grid[nr2][nc2] = "0"
                                queue.append([nr2, nc2])
        
        return n_islands
