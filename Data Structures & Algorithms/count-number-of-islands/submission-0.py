class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def sink(r, c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'   
            
            sink(r + 1, c)
            sink(r - 1, c)
            sink(r, c + 1)
            sink(r, c - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    island_count += 1   
                    sink(i, j)          

        return island_count