#implementation of a stack using a list
#slow compared to using Deque
#lifo
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

#implementatino of a stack using a deque
#faster than using a list
# O(1) time complexity for append and pop
from collections import deque

stack2 = deque()

stack2.append(4)
stack2.append(5)
stack2.append(6)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur = self.head
        out = ""
        while cur:
            out += str(cur.value) + '->'
            cur = cur.next
        return out

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = Node
        self.size += 1

    def pop(self):
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

if __name__ == '__main__':
    print(stack)
    print(stack2)

    for i in range(3):
        print(stack.pop())
        print(stack2.pop())