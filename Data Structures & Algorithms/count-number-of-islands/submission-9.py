class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        def isAllowed(i,j):
            return not (i>(len(grid)-1) or i<0 or j<0 or (j>len(grid[0])-1))

        def buildIsland(coords, isNew):
            nonlocal num_islands
            i = coords[0]
            j = coords[1]
            if not isAllowed(i,j):
                return
            item = grid[i][j]
            if item == "0" :
                return
            else:
                grid[i][j] = "0"
                buildIsland((i,j+1),False)
                buildIsland((i-1,j),False)
                buildIsland((i+1,j),False)
                buildIsland((i,j-1),False)
                if isNew:
                    num_islands +=1

        rownum = 0
        for row in grid:
            for j in range(len(row)):
                buildIsland((rownum,j), True)
            rownum+=1
        return num_islands