"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        row,cols = len(grid),len(grid[0])

        def bfs(r,c):
            rolSpan = r in range(row)
            colSpan = c in range(cols)

            if not rolSpan or not colSpan or (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            area = 1 + (bfs(r+1,c) +
                       bfs(r-1,c) +
                       bfs(r,c+1) +
                       bfs(r,c-1))
            return area

        res = 0
        for r in range(row):
            for c in range(cols):
                res = max(bfs(r,c),res)
        return res
        