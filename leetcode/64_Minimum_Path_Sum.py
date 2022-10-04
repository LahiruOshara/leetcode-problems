class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]
        
        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]
        
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]