class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        num_islands = 0
        def isAllowed(i,j):
            return not (i>(len(grid)-1) or i<0 or j<0 or (j>len(grid[0])-1)) #TODO: Fix helper

        def buildIsland(coords, isNew):
            nonlocal num_islands
            i = coords[0]
            j = coords[1]
            item = grid[i][j]
            if item == "0" or coords in seen:
                return
            else:
                seen.add(coords)
                if isAllowed(i,j+1):
                    buildIsland((i,j+1),False)
                if isAllowed(i-1,j):
                    buildIsland((i-1,j),False)
                if isAllowed(i+1,j):
                    buildIsland((i+1,j),False)
                if isAllowed(i,j-1):
                    buildIsland((i,j-1),False)
                if isNew:
                    num_islands +=1

        for i, row in enumerate(grid):
            for j in range(len(row)):
                buildIsland((i,j), True)
        return num_islands