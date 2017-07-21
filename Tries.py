class Node:
    def __init__(self):
        self.map=dict()
        self.validWord=False

class Tries:
    def __init__(self):
        self.root=Node()
    def insert(self, word):
        cur=self.root
        for i in range(0, len(word)):
            c=word[i]
            if c not in cur.map:
                cur.map[c]=Node()
            cur=cur.map[c]
            if i==len(word)-1:
                cur.validWord=True
    def display(self,cur, level):
        for k,v in cur.map.items():
            print(k, level)
            self.display(v, level+1)
    # def search(self, word):
    #     cur=self.root
    #     for i in range(0,len(word)):
    #         c=word[i]
    #         if c not in cur.map: return False
    #         cur=cur.map[c]
    #         if i==len(word)-1:
    #             return cur.validWord
    #     return False
    def search(self, node, index, word):
        if index==len(word): return node.validWord
        c=word[index]
        if c==".":
            for k,v in node.map.items():
                if self.search(v,index+1,word):
                    return True
            return False
        if c not in node.map: return False
        return self.search(node.map[c],index+1,word)
    def startsWith(self,word):
        cur=self.root
        for i in range(0,len(word)):
            c=word[i]
            if c not in cur.map: return False
            cur=cur.map[c]
        return True
def TriesTest():
    T=Tries()
    T.insert("Hello")
    T.display(T.root)
    # print(T.search("Hello"))
    print(T.search(T.root,0,"H.ll."))

if __name__ == '__main__':
    TriesTest()