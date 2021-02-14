"""
Q1
Given a binary tree, return true if a node's value is the average of all its children (also includes its grandchildren)

Similar question: https://leetcode.com/problems/maximum-average-subtree/
"""
count = 0

class Node:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val

def build_tree():
    root = Node(8/3) # 2.667

    root.right = Node(4)
    root.right.left = Node(2)
    root.right.right = Node(4)

    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)

    return root

def check_if_average(root):
    if not root:
        return 0, 0
    left, n_left = check_if_average(root.left)
    right, n_right = check_if_average(root.right)

    n = n_left + n_right
    avg = (left + right) / (n if n else 1)

    # print(root.val, avg, left, right, n)
    if avg == root.val:
        print(root.val)
        # count += 1

    return root.val + left + right, n+1

root = build_tree()
check_if_average(root)

"""
Q2

You have three unsorted list of numbers.
Design/Write function that will return next minimum element out of these lists (remove that element from list).
Input: list1 = [5, 1, 2, 4], list2 = [4, 6, 3], list3 = [9, 0, 7]
Output:
next(); // 0
next(); // 1
next(); // 2
next(); // 3
next(); // 4
next(); // 4
next(); // 5
next(); // 6
next(); // 7
next(); // 7

Ref: https://leetcode.com/discuss/interview-question/124849/Facebook-or-Sorted-Iterator

The solution is simple if lists are sorted. Build a heap with k elements
next() -> keep popping and adding the next element
hasNext() -> check if PQ is empty
"""

