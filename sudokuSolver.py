class Solution:
    def solveSudoku(self, grid):
        self.cache = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.add_to_cache(grid,row,col)
        self.dfs(grid)
        for row in grid:
            print(row)

    def dfs(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ".":
                    for num in range(1,10):
                        if self.isValid(grid, i, j, str(num)):
                            grid[i][j] = str(num)
                            self.add_to_cache(grid,i,j)
                            if self.dfs(grid):
                                return True
                            self.remove_from_cache(grid,i,j)
                            grid[i][j] = '.'
                    return False
        return True

    def isValid(self, grid, i, j, val):
        return not ((i,val) in self.cache or (val,j) in self.cache or (i//3,j//3,val) in self.cache)

    def add_to_cache(self, grid, i, j):
        val = grid[i][j]
        self.cache.add((i, val))
        self.cache.add((val, j))
        self.cache.add((i//3, j//3, val))

    def remove_from_cache(self, grid, i, j):
        val = grid[i][j]
        self.cache.remove((i, val))
        self.cache.remove((val, j))
        self.cache.remove((i//3, j//3, val))

grid = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(grid)