import collections

"""
https://leetcode.com/discuss/interview-question/390456/Google-or-Phone-Screen-or-Piles-of-Boxes

You are given an array of heights of pile of boxes. You have to return the number of steps
required to bring the height of entire pile to the same height as pile with minimum height.
In one step, you can lower the tallest pile only to the next taller pile.
You can adjust only one pile in a step even though 2 piles could be of same height.
Following examples will illustrate this better,

Example 1:

Input: arrOfHeights = [150, 210, 210, 80, 110]
Output: 9
Explanation:
Step 1 [150, 150, 210, 80, 110]
Step 2 [150, 150, 150, 80, 110]
Step 3 [110, 150, 150, 80, 110]
Step 4 [110, 110, 150, 80, 110]
Step 5 [110, 110, 110, 80, 110]
Step 6 [80, 110, 110, 80, 110]
Step 7 [80, 80, 110, 80, 110]
Step 8 [80, 80, 80, 80, 110]
Step 9 [80, 80, 80, 80, 80]

"""

210 - 2
150 - 1
110 - 1
80 - 1

2
2+1
2+1+1


def pileOfBoxes(boxes):
    store = collections.Counter(boxes).most_common()
    steps = 0; cumulative = 0
    for _, value in store[:-1]:
        steps += value
        cumulative += steps
    return cumulative


boxes = [150, 210, 210, 80, 110]
print(pileOfBoxes(boxes))

boxes = [843, 247]
print(pileOfBoxes(boxes))

boxes = [2]
print(pileOfBoxes(boxes))
