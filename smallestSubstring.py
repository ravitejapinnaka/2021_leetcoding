"""
https://www.pramp.com/challenge/wqNo9joKG6IJm67B6z34

Given an array of unique characters arr and a string str,
Implement a function getShortestUniqueSubstring that finds the smallest substring
of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
"""

def getShortestUniqueSubstring(str, arr):

    pass


def get_shortest_unique_substring(arr, str):
      if not arr or not str:
        return ""
    store, arr, low, high = {}, set(arr), float('inf'), float('-inf')
    res = str+'#'
    for ind in range(len(str)):
        if str[ind] in arr:
        store[str[ind]] = ind
        low, high = min(low, ind), max(high, ind)
        if len(store) == len(arr):
        # low, high = min(store.values()), max(store.values())
        if len(str[low:high+1]) < len(res):
            res = str[low:high+1]
    return res if res != str+'#' else ""

print get_shortest_unique_substring(['x','y','z'], "xyyzyzyx")
print get_shortest_unique_substring(['A'], "")
print get_shortest_unique_substring(['A'], "B")