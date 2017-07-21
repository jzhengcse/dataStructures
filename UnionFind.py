import collections
class UnionFind:
    def __init__(self):
        self.parent=dict()

    def find(self,i):
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


if __name__ == '__main__':
    print(0)


