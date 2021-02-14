"""
https://leetcode.com/discuss/interview-question/1006835/Uber-Reject-Ghosted-or-OA-or-Online-Assessment-or-CodeSignal-or-November-2020
"""
# Author - https://leetcode.com/techdude/

# Question - 1
"""
Given an array A return an output array B of size [A.length - 2] where B[i] = 1 if sides
A[i],A[i+1] and A[i+2] form a triangle. Otherwise, set B[i] = 0.
ex. A = [1, 2, 2, 5, 5, 4] should return B = [1,0,0,1]
"""

A = [1, 2, 2, 5, 5, 4]

def validTriangle(A):
    B = []; i=0
    while i < len(A) - 2:
        a,b,c = A[i], A[i+1], A[i+2]

        if a+b>c and b+c>a and a+c>b:
            B.append(1)
        else:
            B.append(0)
        i += 1
    return B

print(validTriangle(A))
print('*****************************************')

"""
Given two strings a and b, merge the strings so that the letters are added in alternating order
starting with string a. If one string is longer than the other, then append the letters to the end of the merged string.
ex. "abcd", "efghi" -> "aebfcgdhi"
ex. "", "abcd" -> "abcd"
ex. "abcdefg", "zxy" -> "azbxycdefg"
"""

a='abcd'
b = 'efghi'

def mergeStrings(a,b):
    res = ''
    for l1,l2 in zip(a,b):
        res += l1 + l2
    if len(a) < len(b):
        res += b[len(a):]
    elif len(a) > len(b):
        res += a[len(b):]
    return res

print(mergeStrings(a,b)) # aebfcgdhi
a=''; b='abcd'
print(mergeStrings(a,b)) # abcd
a="abcdefg"; b="zxy"
print(mergeStrings(a,b)) # azbxcydefg
print('*****************************************')


"""
Given a string s, return the longest and lexicographically smallest palindromic string
that can be formed from the characters.

ex. "abbaa" -> "abba"
ex. "adeadeadevue" -> "adeeaeeda"
"""

import collections
def smallestPalindrome(str):
    store = collections.Counter(str)
    lexic_store = [[key,val] for key,val in sorted(store.items(), key=lambda x:x[0]) if val > 1]
    lexic_store_single = [[key,val] for key,val in sorted(store.items(), key=lambda x:x[0]) if val % 2 == 1][0][0]

    res = ''
    for key,val in lexic_store:
        res += (key * int(val/2))
    return res + lexic_store_single + res[::-1]

str = "abbaa"
print(smallestPalindrome(str))
str = "adeadeadevue"
print(smallestPalindrome(str))

# OP's solution - similar :)

def smallestPalindromeOP(s):
    if not s:
        return s
    res = []
    counts = collections.Counter(s)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    middle_letter = ""
    for letter in alphabet:
        count = counts.get(letter, 0)
        if count > 0:
            if count % 2 == 1 and middle_letter == "":
                middle_letter = letter
                res.append(letter * ((count - 1) // 2))
            else:
                res.append(letter * (count // 2))

    first = "".join(res)

    return first + middle_letter + first[::-1]

print(smallestPalindromeOP('abbaa'))
print('*****************************************')

# Easy - Medium

"""
Given a list of strings string_list and a list of words words, determine whether each word in words
can be formed as a concatenation of consecutive strings in string_list starting with index 0.
ex. word = "oneTwoThree", string_list = ["one", "Three", "Two"] is false because the words aren't consecutive in string_list
ex. word = "one", string_list = ["one", "Three", "Two"] is True because the concatenation stops at the first index in string_list
ex. word = "one", string_list = ["One", "one", "Two"] is False because the concatenation doesn't start at 0.
Just use the base idea from the LeetCode problem and then modify it for the consecutive concatenation requirement.
It's actually easier than the LeetCode problem.
"""

word = "one"; string_list = ["one", "Three", "Two"]

def isConcatenate(word, string_list):
    res = ''
    for w in string_list:
        res += w
        if res == word:
            return True
    return False

print(isConcatenate(word, string_list))
print('*****************************************')

# Medium

"""
Beauty of a matrix.
Given an n x n matrix M and an int k where n % k == 0,
divide the M into blocks of size k x k starting with the top left corner. i.e.
a 9x9 matrix turns into 9 3x3s. The beauty of a block is the smallest positive number missing
from a block. Rearrange M so that the blocks with the lowest beauty come before those with
higher beauty (top left to bottom right).
In a tie, you should place the block that came first in M before the other block.
"""

matrix = [
    [1,2,2,3],
    [3,4,10,4],
    [2,10,1,2],
    [5,4,4,5],
]

size = 2 # 2 x 2

def get_beauty(sub_matrix):
    sm = sorted(sub_matrix)
    magic_num = 1
    for num in sm:
        if num > magic_num:
            return magic_num
        magic_num += 1
    return magic_num

def magic_number(matrix):
    sub_matrices = []
    serial = 0
    for j in range(size):
        for i in range(size):
            x, y = j * len(matrix)//size, i * len(matrix)//size

            sub_matrix = []
            for p in range(size):
                for q in range(size):
                    sub_matrix.append(matrix[x+p][y+q])

            beauty_num = get_beauty(sub_matrix)
            sub_matrices.append([sub_matrix, beauty_num, serial])
            serial += 1

    sub_matrices.sort(key=lambda x: (x[1],x[2]))

    serial = 0
    for j in range(size):
        for i in range(size):
            x, y = j * len(matrix)//size, i * len(matrix)//size

            iter1 = iter(sub_matrices[serial][0])
            for p in range(size):
                for q in range(size):
                    matrix[x+p][y+q] = next(iter1)
            serial += 1

    for row in matrix:
        print(row)

    return matrix

magic_number(matrix)

print('*****************************************')

"""
Rotate matrix around diagonals.
Given an n x n matrix M, where n is odd and n > 1, and an integer k,
rotate M counterclockwise k times which are not on the main diagonal or
on the diagonal from the top right to the bottom left.
Return the new matrix.
Ex. I put *s to show which elements are fixed on the diagonals.

[*1*, 2, 3, 4, *5*]
[6, *7*, 8, *9*, 10]
[11, 12, *13*, 14, 15]
[16, *17*, 18, *19*, 20]
[*21*, 22, 23, 24, *25*]

Rotates to:

[*1*, 16, 11, 6, *5*]
[22, *7*, 12, *9*, 2]
[23, 18, *13*, 8, 3]
[24, *17*, 14, *19*, 4]
[*21*, 20, 15, 10, *25*]
"""


# Brilliant method - https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image

#  * clockwise rotate
#  * first reverse up to down, then swap the symmetry
#  * 1 2 3     7 8 9     7 4 1
#  * 4 5 6  => 4 5 6  => 8 5 2
#  * 7 8 9     1 2 3     9 6 3

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def reverseImage(matrix):
    start, end = 0, len(matrix)-1

    while start < end:
        for i in range(len(matrix)):
            if start != i and end!= i:
                matrix[start][i], matrix[end][i] = matrix[end][i], matrix[start][i]
        start += 1
        end -= 1
    return matrix

def swapMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if i != j and i+j != len(matrix) -1:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def rotateImage(matrix, num_rotate):
    num_rotate = num_rotate % 4 # because 4 rotations = original image

    for _ in range(num_rotate):
        matrix = reverseImage(matrix)
        matrix = swapMatrix(matrix)

    return matrix

print(rotateImage(matrix, 17))

# Medium/Hard
"""
Given two arrays a and b of equal length,
the absolute sum difference is the sum Math.abs(a[i] - b[i]).
Replace one number in a with any number in a to minimize the absolute sum difference.

ref: https://leetcode.com/discuss/interview-question/949484/codesignal-gca-i-have-a-question
idea: https://leetcode.com/discuss/interview-question/949484/CodeSignal-GCA-(I-have-a-question)/779839
"""

arr1 = [1,2,3,4]
arr2 = [1,2,4,0]

def find_in_arr1(num, arr):
    return min(arr, key=lambda x:abs(x[0]-num))[1]

def minAbsSumDiff(arr1, arr2):
    sorted_arr1 = [(num,i) for i, num in enumerate(sorted(arr1))]
    min_diff_sum = orig_sum_diff = sum([abs(num1 - num2) for num1, num2 in zip(arr1, arr2)])

    for i, num in enumerate(arr1):
        index = find_in_arr1(arr2[i], sorted_arr1)
        if index != i:
            min_diff_sum = min(min_diff_sum, orig_sum_diff - (abs(arr1[i]-arr2[i])) + (abs(arr1[index] - arr2[i])))

    return min_diff_sum

print(minAbsSumDiff(arr1, arr2))

