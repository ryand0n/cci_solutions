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

    def removeDupes(self):
        unique_vals = set()
        cur = self.head
        prev = None

        while (cur):
            if cur.data not in unique_vals:
                unique_vals.add(cur.data)
            elif cur.data in unique_vals:
                prev.next = cur.next

            prev = cur
            cur = cur.next

    def length(self):
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next
        return length

    def kthToLast(self, k):
        length = self.length()
        stop_index = length - (k + 1)
        index = 0
        cur = self.head
        while cur:
            if index == stop_index:
                return cur.data
            index += 1
            cur = cur.next

    def deleteMiddleNode(self, node):
        prev = None
        cur = self.head
        while cur:
            if cur.data == node:
                prev.next = cur.next

            prev = cur
            cur = cur.next

    def partition(self, x):
        less_head = less_tail = Node(0)
        greater_head = greater_tail = Node(0)
        head = self.head
        
        while head:
            if head.val < x:
                less_tail.next = head
                less_tail = head
            else:
                greater_tail.next = head
                greater_tail = head
            head = head.next
        
        greater_tail.next = None
        less_tail.next = greater_head.next
        
        return less_head.next

    def palindrome(self):
        contents = []
        cur = self.head
        while cur:
            contents.append(cur.data)
            cur = cur.next

        return contents == contents[::-1]

    def loop_detection(self):
        cur = self.head
        while cur:
            if cur.next == self.head:
                return cur.data
            cur = cur.next

def sumLists(head1, head2):
    number_1 = ""
    while head1:
        number_1 += str(head1.data)
        head1 = head1.next

    number_2 = ""
    while head2:
        number_2 += str(head2.data)
        head2 = head2.next

    ans_ll = LinkedList()
    ans = int(number_1[::-1]) + int(number_2[::-1])
    ans_ll.head = Node(str(ans)[::-1][0])
    prev = ans_ll.head

    for val in str(ans)[::-1][1:]:
        cur = Node(val)
        prev.next = cur
        prev = cur

    return ans_ll


def intersect(headA, headB):
    lenA, lenB = 0, 0
    currA, currB = headA, headB
    
    while currA:
        lenA += 1
        currA = currA.next
    while currB:
        lenB += 1
        currB = currB.next
    
    currA, currB = headA, headB
    if lenA > lenB:
        for i in range(lenA - lenB):
            currA = currA.next
    else:
        for i in range(lenB - lenA):
            currB = currB.next
    
    while currA and currB:
        if currA == currB:
            return True
        currA = currA.next
        currB = currB.next
        
    return False



linked = LinkedList()
linked.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
dupe_1 = Node(3)
dupe_2 = Node(1)
dupe_3 = Node(6)

linked.head.next = dupe_1
dupe_1.next = second
second.next = third
third.next = fourth
fourth.next = dupe_2
dupe_2.next = fifth
fifth.next = sixth
sixth.next = dupe_3

# linked.removeDupes()
# linked.printList()
# linked.partition(4)
# linked.printList()

x = LinkedList()
x.head = Node(7)
x1 = Node(1)
x2 = Node(7)

x.head.next = x1
x1.next = x2

y = LinkedList()
y.head = Node(5)
y1 = Node(9)
y2 = Node(2)

y.head.next = y1
y1.next = y2

# ans = sumLists(x.head, y.head)
# ans.printList()

print(x.palindrome())
    