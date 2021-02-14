"""
https://www.geeksforgeeks.org/find-number-distinct-palindromic-sub-strings-given-string/

Find all distinct palindromic sub-strings of a given string

Given a string of lowercase ASCII characters, find all distinct continuous palindromic sub-strings of it.

Examples:

Input: str = "abaaa"
Output:  Below are 5 palindrome sub-strings
a
aa
aaa
aba
b


Input: str = "geek"
Output:  Below are 4 palindrome sub-strings
e
ee
g
k
"""

def palindromicSusbtrings(s):
    result = set()
    for i in range(len(s)):
        result |= extendPal(s, i,i) | extendPal(s, i, i+1)
    return result

def extendPal(s, start, end):
    tmp =set()
    while start >= 0 and end < len(s) and s[start] == s[end]:
        tmp.add(s[start:end+1])
        start -= 1; end += 1
    return tmp



print(palindromicSusbtrings('abaaa'))