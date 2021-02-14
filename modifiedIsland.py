"""
https://leetcode.com/discuss/interview-question/872735/Roblox-Karat-Interview

Find the top left and bottom right coordinates of a rectangle of 0's
within a matrix of 1's. It's essentially a modified version of the finding the
number of island problem where you only need to dfs to the right and down.
Ex.
[[ 1, 1, 1, 1],
[ 1, 0, 0, 1],
[ 1, 0, 0, 1],
[ 1, 1, 1, 1]]
Expected output: [[1,1], [2,2]]

"""
grid = [[ 1, 1, 1, 1],[ 1, 0, 0, 1],[ 1, 0, 0, 1],[ 1, 1, 1, 1]]

def solve(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                start = [i,j]

                p, q = i, j
                while grid[p][q] == 0:
                    p+=1
                while grid[p-1][q] == 0:
                    q+=1

                # end = []
                # dfs(grid, i, j, end)
                return start, [p-1,q-1]
    return -1, -1


def dfs(grid, i, j, end):
    north = grid[i-1][j] if i-1>=0 else 1
    south = grid[i+1][j] if i+1<len(grid) else 1
    east = grid[i][j+1] if j+1<len(grid[0]) else 1
    west = grid[i][j-1] if j-1>=0 else 1

    print(i,j, north, south, east, west)
    if north == south == east == west == 1:
        end = [i,j]
    # print(i,j)

    grid[i][j] = '#'

    for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
        if 0<=i+di<len(grid) and 0<=j+dj<len(grid[0]) and grid[i+di][j+dj] == 0:
            dfs(grid, i+di, j+dj, end)


print(solve(grid))
