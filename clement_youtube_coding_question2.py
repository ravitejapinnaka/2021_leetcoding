import collections

source = "https://www.youtube.com/watch?v=JHzX-57dgn0&t=172s"

"""
Find all the occurences of permutations of smallString in the bigString
Answer: ["cba", "abc", "bca", "cab", "abc", "bca"]
Just return length of the array
"""

bigString = "cbabcacabca"
smallString = "abc"

def findPermutations(bigString, smallString):
    store = collections.Counter(smallString)
    counter = len(smallString)
    start = end = 0
    answer = 0
    while end < len(bigString):
        letter = bigString[end]
        if letter in store:
            # store[letter] -= 1
            counter -= 1

        while counter == 0:
            answer += 1

            start += 1
            end += 1
            counter = len(smallString)
            # TO BE COMPLETED





findPermutations(bigString,smallString)