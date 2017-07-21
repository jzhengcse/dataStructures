class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class linkedList:
    def __init__(self):
        self.head=None

    def printNode(self):
        while self.head!=None:
            print(self.head.val)
            self.head=self.head.next
    def insertHead(self,node):
        node.next=self.head
        self.head=node
    def insertAtIndex(self,i,node):
        if i==0:
            self.insertHead(node)
        else:
            cur=self.head
            for k in range(0,i-1):
                cur=cur.next
            if cur==None: return
            node.next=cur.next
            cur.next=node

    def deleteHead(self,):
        if self.head==None: return
        self.head=self.head.next

    def deleteAtIndex(self,i):
        if i==0:
            self.deleteHead()
        else:
            cur=self.head
            for i in range(0,i-1):
                cur=cur.next
            if cur==None: return
            if cur.next==None: return
            cur.next=cur.next.next

def nodeTest():
    myList=linkedList()
    myList.insertHead(Node(1))
    myList.insertAtIndex(1,Node(2))
    #myList.deleteHead()
    myList.deleteAtIndex(1)
    myList.printNode()

if __name__ == '__main__':
    nodeTest()