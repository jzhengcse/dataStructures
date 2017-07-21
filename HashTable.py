from random import randint
class hash:
    def __init__(self):
        self.p=10000019
        self.a=randint(1,self.p-1)
        self.b=randint(0,self.p-1)
        self.x=randint(1,self.p-1)

    def hString(self, str,size):
        hash=0
        for i in str:
            hash=(hash*self.x+ord(i))%self.p
        return self.h(hash,size)

    def h(self,key,size):
        return ((self.a*key+self.b)%self.p)%size
class HashTable:
    def __init__(self):
        self.m=10
        self.T=[[] for i in range(0,self.m)]
        self.size=0
        self.hash=hash()

    def h(self, key):
        return self.hash.hString(key,len(self.T))
    def hasKey(self, key):
        hash=self.h(key)
        L=self.T[hash]
        for k,v in L:
            if k==key:
                return True
        return False
    def get(self, key):
        hash=self.h(key)
        L=self.T[hash]
        for k,v in L:
            if k==key:
                return v
        return None

    def set(self, key, value):
        hash=self.h(key)
        L=self.T[hash]
        for i in L:
            if i[0]==key:
                i[1]=value
                return
        self.size += 1
        L.append([key,value])
        self.rehash()

    # decrease the size
    def remove(self, key):
        hash=self.h(key)
        L=self.T[hash]
        for i in range(0,len(L)):
            p=L[i]
            if p[0]==key:
                del L[i]
                return
    def printMap(self):
        for i in range(0,len(self.T)):
            L=self.T[i]
            print(i)
            for k,v in L:
                print("{}-->{}".format(k,v))

    def rehash(self):
        loadFactor=self.size/len(self.T)
        # print(loadFactor)
        if loadFactor>0.9:
            T2 = [[] for i in range(0, 2*len(self.T))]
            self.hash=hash()
            self.size = 0
            temp=self.T
            self.T=T2
            for L in temp:
                for k,v in L:
                    self.set(k,v)
def hashTest():
    map=HashTable()
    for i in ["adsd","bdfsfs","csfsdfs"]:
        map.set(i,20)
    # print(map.hash.a)
    # print(map.hash.b)
    # map.set(10,20)
    # print(map.hash.a)
    # print(map.hash.b)



    # map.set(5,30)
    # print(map.size)
    # map.remove(5)
    # print(map.hasKey(10))
    map.printMap()

    # map.rehash()

    # map.printMap()
if __name__ == '__main__':
    hashTest()

# HasKey()
# Get(O)
# Set(O,v)