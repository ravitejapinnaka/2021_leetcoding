"""
if you dont do this in the first attempt, dont call yourself a coder!!

Result - not calling :( !!
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def build_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    return head

def reverseList(head):
    if not head:
        return head
    prev = None
    current = head
    nxt = head.next

    while current:
        current.next = prev
        prev = current
        current = nxt
        nxt = current.next if current else None
    return prev


print(reverseList(build_list()).val)