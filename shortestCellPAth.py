def shortestCellPath(grid, sr, sc, tr, tc):
    q = [((sr, sc), 0)]
    # visited = set()
    
    while q:
        source, level = q.pop(0)
        grid[source[0]][source[1]] = 0
        if source == (tr, tc):
            return level

        for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
            x,y = source
            p, q1 = x + direction[0], y+direction[1]
            if isSafe(grid, p, q1):
                q.append(((p,q1), level+1))

    return -1


def isSafe(grid, p, q):
    return 0<= p < len(grid) and 0<=q<len(grid[0]) and grid[p][q] == 1

  
grid = [[1, 1, 1, 1],[0, 0, 0, 1],[1, 1, 1, 1]]
sr = 0; sc = 0; tr = 2; tc = 0
print(shortestCellPath(grid, sr, sc, tr, tc))


100
110
110