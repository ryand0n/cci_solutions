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

class SetofStacks(Stack):
    def __init__(self, threshold=5):
        super().__init__()
        self.threshold = threshold
        self.all_stacks = []
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        if len(self.stack) == self.threshold:
            self.all_stacks.append(self.stack)
            self.stack = []

    def pop(self):
        last_stack = self.all_stacks[-1]
        return last_stack.pop(len(last_stack) - 1)

    def popAt(self, index):
        cnt = 0
        for i in range(len(self.all_stacks)):
            for j in range(len(self.all_stacks[i])):
                if cnt == index:
                    return self.all_stacks[i].pop(j)
                cnt += 1

class Stack():
    def __init__(self):
        self.stack = deque()
        self.size = len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop(len(self.stack) - 1)

class MyQueue():
    def __init__(self):
        self.one = []
        self.two = []

    def push(self, value):
        self.one.append(value)

    def pop(self, value):
        if not self.one:
            while self.one:
                self.two.append(self.one.pop())
        return self.two.pop()

class SortStack():
    def __init__(self) -> None:
        self.storage = [] # additional stack
        self.smallest = 0

    def push(self, value):
        self.storage.append(value)
        self.storage.sort(reverse=True)

    def pop(self):
        return self.storage.pop() 

class AnimalShelter():
    def __init__(self) -> None:
        self.age = {}
        self.storage = []

    def update_age(self):
        for i in range(len(self.storage)):
            self.age[i] == len(self.storage) - i

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.pop(0)

    def dequeueAnimal(self, pet):
        for i in range(len(self.storage)):
            if self.storage[i] == pet:
                return self.storage.pop(i)

queue = AnimalShelter()
queue.enqueue('dog')
queue.enqueue('cat')
queue.enqueue('dog')
queue.enqueue('dog')

queue.dequeueAnimal('cat')

print(queue.storage)



# stack = SetofStacks()
# for i in range(25):
#     stack.push(i)

# print(stack.all_stacks)
# print(stack.pop())
# print(stack.popAt(10))
# print(stack.all_stacks)

