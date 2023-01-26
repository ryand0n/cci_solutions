
from unittest.loader import VALID_MODULE_NAME
from matplotlib.colors import TwoSlopeNorm

from matplotlib.pyplot import thetagrids


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        #prints the LL
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        #pushes node to the front of the LL
        #O(1)
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        #add node in the middle of the LL
        #O(n) - time
        #O(1) - space
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        #add node to end of LL
        #O(n) - time
        #O(1) - can be 1 if there is a tail attribute
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node

    def delete(self, key):
        #deletes node
        #O(n) - time
        #O(1) - space
        temp = self.head

        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return
        
        prev.next = temp.next
        temp = None

    def delete_position(self, position):
        #delete node at a certain index
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    def deleteList(self):
        #delete the entire LL
        #self.head = None would also work
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev

    def length(self):
        #returns length of LL
        #O(n) - time
        #O(1) - space
        count = 0
        current = self.head
        while (current is not None):
            current = current.next
            count += 1
        print("the length of the LL is: " + str(count))
        return count

    def length_recursive(self, node):
        #returns length of LL but recursively
        if node is None:
            return 0
        else:
            return 1 + self.length_recursive(node.next)

    def search(self, key):
        #searches for a node
        #O(n) - time
        #O(1) - space
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def search_recur(self, node, key):
        #searches for a node recursively
        if node is None:
            return False
        if node.data == key:
            return True
        else:
            return self.search_recur(node.next, key)

    def get_value(self, index):
        #returns the value at a certain index
        #O(n) - time
        #O(1) - space
        count = 0
        current = self.head
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1

    def count_recur(self, node, value):
        #returns count of certain value in LL recursively
        if node is None:
            return 0
        if node.data == value:
            return 1 + self.count(node.next, value)
        return self.count(node.next, value)

    def count(self, value):
        #returns count of certain value in LL
        #O(n) - time
        #O(1) - space
        current = self.head
        count = 0
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

    def reverse(self):
        #reverse a LL
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


def intersection(a, b):
        #returns values that are in both sorted LL
        #O(m + n) - time
        #O(max(m,n)) - space
        result = Node(0)
        curr = result

        while (a != None and b != None):
            if a.data == b.data:
                curr.next = Node(a.data)
                curr = curr.next

                a = a.next
                b = b.next
            elif a.data < b.data:
                a = a.next
            else:
                b = b.next
        result = result.next
        return result

def printList(temp):
        #prints the LL
        while (temp):
            print(temp.data)
            temp = temp.next

def reverse(node):
    prev = None
    curr = node.head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    

if __name__ == '__main__':
    linked = LinkedList()
    linked.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)

    linked.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth

    linked.reverse()
    printList(linked.head)







    
