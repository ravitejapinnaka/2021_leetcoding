"""
https://leetcode.com/problems/valid-sudoku/
"""

# class Solution:
#     # def isValidSudoku(self, grid: List[List[str]]) -> bool:
#     def isValidSudoku(self, grid):
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 # print(i,j,grid[i][j])
#                 if grid[i][j] == ".":
#                     for num in range(1,10):
#                         grid[i][j] = str(num)
#                         if self.isValid(grid, i, j):
#                             self.printt(grid)
#                             if self.isValidSudoku(grid):
#                                 return True
#                             grid[i][j] = '.'
#         return False

#     def printt(self, grid):
#         for row in grid:
#             print(row)
#         print('**********************************')

#     def isValid(self, grid, i, j):
#         return self.isRowValid(grid,i,j) and self.isColumnValid(grid,i,j) and self.isSubValid(grid,i,j)

#     def isRowValid(self, grid, i, j):
#         nums = set()
#         for j in range(len(grid[0])):
#             if grid[i][j] in nums:
#                 return False
#             if grid[i][j] != '.':
#                 nums.add(grid[i][j])
#         return True

#     def isColumnValid(self, grid, i, j):
#         nums = set()
#         for i in range(len(grid)):
#             if grid[i][j] in nums:
#                 return False
#             if grid[i][j] != '.':
#                 nums.add(grid[i][j])
#         return True

#     def isSubValid(self, grid, p, q):
# #         4,6
#         nums = set()
#         m, n = int(p/3), int(q/3) #1,2
#         for i in range(3*m, 3*m+3):
#             for j in range(3*n, 3*n+3):
#                 if grid[i][j] in nums:
#                     return False
#                 if grid[i][j] != '.':
#                     nums.add(grid[i][j])
#         return True

class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self,board):
        if not board:return False
        m,n=len(board),len(board[0])
        check_row=[[0 for i in range(9)] for j in range(9)]#three 2d array to check each row, col and sub box
        check_col=[[0 for i in range(9)] for j in range(9)]#three 2d array to check each row, col and sub box
        check_box=[[0 for i in range(9)] for j in range(9)]#three 2d array to check each row, col and sub box
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    num=int(board[i][j])-1 # need -1 becasue the index of array is 0~8
                    k=i/3*3+j/3
                    #because if previously the same number of same row,col or box have exist, it is false
                    if check_row[i][num] or check_col[j][num] or check_box[k][num]:
                        return False
                    #assign value to all the checking 2d arrayes

                    check_row[i][num]=check_col[j][num]= check_box[k][num]=1
        return True
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","5","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))

# print(board[0][0][0])
# kk = [[j for j in range(5)] for i in range(4)]
# print(kk)
# print(kk[0][0])