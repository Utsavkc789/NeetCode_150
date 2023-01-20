"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid),len(grid[0])
        visited = set()
        islands = 0

        def explore(r,c,visited):
            rowInbound = r in range(rows)
            colInbound = c in range(cols)

            if not rowInbound or not colInbound or grid[r][c] == "0" or (r,c) in visited:
                return False
                
            visited.add((r,c))

            explore(r-1,c,visited)
            explore(r+1,c,visited)
            explore(r,c-1,visited)
            explore(r,c+1,visited)
            return True

        for r in range(rows):
            for c in range(cols):
                if explore(r,c,visited):
                    islands+=1
        return islands