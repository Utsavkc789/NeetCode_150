"""

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
           ROW,COL = len(heights),len(heights[0])
           pac,alt=set(),set()

           def dfs(r,c,visited,prevHeight):
                rowSpan = r in range(ROW)
                colSpan = c in range(COL)
                if not rowSpan or not colSpan or (r,c) in visited or prevHeight > heights[r][c]:
                    return 
                visited.add((r,c))

                dfs(r+1,c,visited,heights[r][c])
                dfs(r-1,c,visited,heights[r][c])
                dfs(r,c+1,visited,heights[r][c])
                dfs(r,c-1,visited,heights[r][c])

            # going through the border columns to find all that connect to the pacific and atlantic
           for c in range(COL):
                dfs(0,c,pac,heights[0][c])
                dfs(ROW-1,c,alt,heights[ROW-1][c])

            # going through the border rows to find all that connect to the pacific and atlantic   
           for r in range(ROW):
                dfs(r,0,pac,heights[r][0])
                dfs(r,COL-1,alt,heights[r][COL-1])
            
            
           res = []
           for r in range(ROW):
               for c in range(COL):
                   # checking if they exist in both pacific and atlantic set
                   if (r,c) in pac and (r,c) in alt:
                        res.append([r,c])
           return res


