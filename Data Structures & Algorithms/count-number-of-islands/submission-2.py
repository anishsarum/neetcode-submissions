class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        ROWS = len(grid)
        COLS = len(grid[0])

        n_islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    queue = deque([(r, c)])
                    n_islands += 1
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for dr, dc in DIRECTIONS:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr, nc))
        
        return n_islands
