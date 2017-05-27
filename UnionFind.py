import collections
class UnionFind:
    def __init__(self):
        self.parent=dict()
        self.count=0

    def add(self,m,n,node):
        self.parent[node]=node
        self.count+=1
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        print(node)
        x=node[0]
        y=node[1]
        for i in range(0,4):
            newX=x+dx[i]
            newY=y+dy[i]
            if newX<0 or newX>=m: continue
            if newY<0 or newY>=n: continue
            if (newX,newY) not in self.parent: continue
            if self.find(node)!=self.find((newX,newY)):
                self.count-=1
                self.union(node,(newX,newY))
    def init(self,nums):
        self.parent=dict()
        for i in nums:
            self.parent[i]=i
    def find(self,i):
        # print(i)
        # print("self parent {}".format(self.parent[i]))
        if i!=self.parent[i]:
            self.parent[i]=self.find(self.parent[i])
        return self.parent[i]

    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if px!=py:
            self.parent[py]=px
    def print(self):
        for k,v in self.parent.items():
            print("{}:{}".format(k,v))

def UnionFindTest():
    nums=[2,1,3,5,4]
    UF=UnionFind(nums)
    for i in nums:
        # print(i-1 in UF.parent)
        if i-1 in UF.parent:
            UF.union(i,i-1)
        if i+1 in UF.parent:
            UF.union(i,i+1)
    pa=[]
    for k in UF.parent.keys():
        pa.append(UF.find(k))
    map1 = collections.Counter(pa)
    print(max(map1.values()))
def validTree(n, edges):

    # init the UnionFind
    mySet=set()
    for e in edges:
        a=e[0]
        b=e[1]
        mySet.add(a)
        mySet.add(b)
    UF=UnionFind(mySet)

    # not cycle
    for e in edges:
        a=e[0]
        b=e[1]
        if UF.find(a)==UF.find(b):
            print("not a tree")
            return False
        UF.union(a,b)

    # only one root
    pa=set()
    for k in UF.parent.keys():
        pa.add(UF.find(k))
    print(pa)
    return len(pa)==1

def validTreeTest():
    n=4
    edges=[[0,1],[0,2],[2,3],[2,4]]
    validTree(n,edges)

def numIslands2(m, n, positions):
    UF=UnionFind()
    for p in positions:
        UF.add(m,n,tuple(p))
        print(UF.count)
        # UF.print()
def numIslands2Test():
    m=3
    n=3
    positions=[[0,0], [0,1], [1,2], [2,1]]
    numIslands2(m,n,positions)
if __name__ == '__main__':
    numIslands2Test()


