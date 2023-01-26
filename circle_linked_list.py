class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.last = None

    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data, end = " ")
                temp = temp.next
                if temp == self.head:
                    break

    def push(self, new_data):
        new_start = Node(new_data)
        temp = self.head
        new_start.next = self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_start
        else:
            new_start.next = new_start
        self.head = new_start

    def addToEmpty(self, data):
        #adding to empty LL
        temp = Node(data)
        self.head = temp
        self.head.next = self.head
        return self.head

    def getLast(self):
        #gets tail of LL
        temp = self.head
        while True:
            if temp.next == self.head:
                return temp
            temp = temp.next

    def addFront(self, data):
        #adding to front of LL
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.head = temp

    def addBack(self, data):
        #adding to the back of the LL
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp

    def addMiddle(self, data, item):
        #adding to the middle of the LL
        temp = Node(data)
        curr = self.head
        while curr:
            if curr.data == item:
                temp.next = curr.next
                curr.next = temp
                break
            curr = curr.next 

    def delete(self, item):
        #deletes node in the middle of LL 
        curr = self.head
        prev = None
        while curr:
            if curr.data == item:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next

class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enQueue(self, value):
        temp = Node(value)
        #if queue is empty
        if self.head == None:
            self.head = temp
            self.last = temp
            self.head.next = self.last
            self.last.next = self.head
        else:
            self.last.next = temp
            temp.next = self.head
            self.last = temp

    def deQueue(self):
        if self.head == self.last:
            ans = self.head
            self.head = None
            self.last = None
            return ans
        else:
            ans = self.head
            self.last.next = self.head.next
            self.head = self.last.next
            return ans

    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data, end = " ")
                temp = temp.next
                if temp == self.head:
                    break
    

x = CircularLinkedList()
x.push(4)
x.push(3)
x.push(2)
x.push(1)
x.last = x.getLast()
x.addFront(20)
x.addBack(40)
x.addMiddle(80, 3)
x.delete(3)
x.printList()
print('\n')

q = Queue()
q.enQueue(14)
q.enQueue(22)
q.enQueue(-6)
q.printList()
print('\n')
q.deQueue()
q.deQueue()
q.enQueue(9)
q.enQueue(20)
q.printList()

    

