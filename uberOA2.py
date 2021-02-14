"""
https://leetcode.com/discuss/interview-question/928723/Uber-or-OA-or-CodeSignal
"""

# Q1: Given an int, find alternate digit sum, reversing signs.
# For example input 52413, output {5 + (-2) + 4+ (-1) + 3}

def alternateSum(num):
    asum = 0
    for i, n in enumerate(str(num)):
        if i%2:
            asum += -int(n)
        else:
            asum += int(n)
    return asum

def alternateSum2(num):
    asum = 0; cnt = 0;
    while num:
        x = num % 10 if cnt % 2 == 0 else -(num % 10)
        asum += x
        num //= 10
        cnt += 1
    return asum if cnt % 2 else -asum

num = 52413
print(alternateSum(num))
print(alternateSum2(num))

# Q2. Prefix String - given two string arrays A & B, find if all strings
# in B are prefixes of a concatenation of strings in A.
# For example if A = {"one", "two", "three"} B = {"onetwo", "one"}, return True

def findPrefixString(B, A):
    for word in B:
        print(helperDFS(word, set(A), ''))
        if not helperDFS(word, set(A), ''):
            return False
    return True

def helperDFS(word, prefixes, path):
    if len(path) >= len(word):
        if path == word:
            return True
        return False

    for w in prefixes:
        if helperDFS(word, prefixes, path + w):
            return True
    return False

A = ["one", "two", "three"]; B = ["onetwo", "one", "onethree", "onethre"]
print(findPrefixString(B,A))

# Q3. Rotate n * m matrix clockwise k times around main diagonals. i.e
# keep items on main diagonals as it is.

# Refer to "rotateImage" in uberCodeSignal.py

# Q4. Given matrix where each cell's value is corresponding (row * col)
# value and all cells are alive initially, and given a 2d array of queries such that:
# [0] means return minimum value left in matrix
# [1, i] means kill all cells in row i
# [2, j] means kill all cells in colomn j
# return an array of output of these queries.