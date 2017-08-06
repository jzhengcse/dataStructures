import sys

class priorityQueue:

    def __init__(self):
        self.maxSize=100
        self.size=0
        self.A=[0 for i in range(0,self.maxSize)]

    def parent(self,i):
        return (i-1)//2
    def leftChild(self,i):
        return 2*i+1
    def rightChild(self,i):
        return 2*i+2

    def insert(self,key):
        if self.size==self.maxSize: return
        self.A[self.size]=key
        self.siftup(self.size)
        self.size+=1

    def siftup(self,i):
        while i>0 and self.A[i]>self.A[self.parent(i)]:
            swap(self.A,i,self.parent(i))
            i=self.parent(i)

    def print(self):
        for i in range(0,self.size):
            print(self.A[i])

    def extractMax(self):
        self.A[0]=self.A[self.size-1]
        self.size-=1
        self.siftDown(0)

    def siftDown(self,i):
        while self.leftChild(i) < self.size:
            maxIndex = i
            left = self.leftChild(i)
            right = self.rightChild(i)
            if left < self.size and self.A[left] > self.A[maxIndex]:
                maxIndex = left
            if right < self.size and self.A[right] > self.A[maxIndex]:
                maxIndex = right
            if maxIndex == i: break
            swap(self.A, i, maxIndex)
            i = maxIndex

    def getMax(self):
        return self.A[0]

    def remove(self,i):
        self.A[i]=sys.maxsize
        self.siftup(i)
        self.extractMax()

    def changePriority(self,i,key):
        old=self.A[i]
        self.A[i]=key
        if key>old:
            self.siftup(i)
        elif key<old:
            self.siftDown(i)


def swap(A,a,b):
    temp=A[a]
    A[a]=A[b]
    A[b]=temp

def testQ():
    q=priorityQueue()
    #print(q.parent(3))
    #print(q.parent(5))
    #print(q.leftChild(1))
    #print(q.rightChild(2))
    q.insert(4)
    q.insert(2)
    q.insert(6)
    q.insert(9)
    q.print()
    #q.extractMax()
    #q.print()
    #q.extractMax()
    #q.print()
    #q.extractMax()
    #q.print()
    #q.extractMax()
    #q.print()
    #q.remove(1)
    #q.print()
    q.changePriority(1,1)
    q.print()


if __name__ == '__main__':
    testQ()
    ## add comment
