class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class arrayQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.size=4
        self.A=[0 for i in range(0,self.size)]
    def enqueue(self,val):
        if self.full(): return
        self.A[self.rear]=val
        print("enqueue: {} at {}".format(val,self.rear))
        self.rear=(self.rear+1)%self.size
    def dequeue(self):
        if self.empty(): return
        #print("not empty")
        self.front=(self.front+1)%self.size
        #print("update front to: {}".format(self.front))
    def empty(self):
        return self.front==self.rear
    def full(self):
        return (self.rear+1)%self.size==self.front
    def print(self):
        #print(self.A)
        front=self.front
        rear=self.rear
        print("front {} rear {}".format(front,rear))
        while front!=rear:
            print(self.A[front])
            front=(front+1)%self.size
def queueTest():
    iQueue=arrayQueue()
    iQueue.enqueue(1)
    iQueue.enqueue(2)
    iQueue.enqueue(3)
    iQueue.print()
    iQueue.dequeue()
    iQueue.print()
    iQueue.dequeue()
    iQueue.print()
    iQueue.dequeue()
    iQueue.print()
    iQueue.enqueue(1)
    iQueue.enqueue(2)
    iQueue.enqueue(3)
    iQueue.print()

class arrayStack:
    def __init__(self):
        self.A=[]
        self.top=-1
    def push(self,val):
        self.A.append(val)
        self.top+=1
    def pop(self):
        if self.top==-1: return
        re=self.A[self.top]
        self.top-=1
        return re
    def top(self):
        return self.A[self.top]
    def empty(self):
        self.top==-1
    def print(self):
        for i in range(0,self.top+1):
            print(self.A[i])

def arrayStackTest():
    istack=arrayStack()
    istack.push(1)
    istack.push(2)
    istack.print()
    istack.pop()
    istack.print()
    istack.pop()
    istack.print()
    istack.pop()



class listStack():
    def __init__(self):
        self.head=None
    def push(self,node):
        node.next = self.head
        self.head = node
    def pop(self):
        if self.head==None: return
        self.head = self.head.next
    def empty(self):
        return self.head==None

def listStackTest():
    myStack=listStack()
    myStack.push(Node(1))
    myStack.push(Node(2))
    myStack.pop()
    printNode(myStack.head)
    myStack.pop()
    myStack.pop()

class listQueue():
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,Node):
        if self.head==None:
            self.head=Node
            self.tail=Node
        else:
            self.tail.next=Node
            self.tail=Node

    def dequeue(self):
        if self.head==None: return
        re=self.head
        self.head=self.head.next
        print(re.val)
        return re

    def print(self):
        cur=self.head
        while cur!=None:
            print(cur.val)
            cur=cur.next

    def empty(self):
        return self.head==None
def listQueueTest():
    myQueue=listQueue()
    myQueue.enqueue(Node(1))
    myQueue.enqueue(Node(2))
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    print(myQueue.empty())
    myQueue.print()
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printNode(head):
    cur=head
    while cur!=None:
        print(cur.val)
        cur=cur.next

if __name__ == '__main__':
    listQueueTest()
