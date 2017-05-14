import pickle
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def readwrite():
    node=TreeNode(1)
    node.left=TreeNode(0)
    node.right=TreeNode(1)
    f=open("input.txt","wb")
    pickle.dump(node,f)
    f.close()

    f=open("input.txt","rb")
    node=pickle.load(f)
    f.close()
    inorder(node)


def searchNode(root, node):
    if root == None: return False
    if node.val == root.val:
        return True
    elif node.val > root.val:
        return searchNode(root.right, node)
    else:
        return searchNode(root.left, node)


def insertNode(root, node):
    if root == None: return node
    if node.val > root.val:
        root.right = insertNode(root.right, node)
    else:
        root.left = insertNode(root.left, node)
    # print(root.val)
    return root


def deleteNode(root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    dummy = TreeNode(0)
    dummy.right = root
    p = dummy
    cur = root
    # find the node and it's parent
    while cur != None:
        if key == cur.val:
            break
        elif key > cur.val:
            p = cur
            cur = cur.right
        else:
            p = cur
            cur = cur.left

    # can't find node return the root
    if cur == None: return dummy.right
    # no child
    if cur.left == None and cur.right == None:
        if cur == p.left:
            p.left = None
        else:
            p.right = None
    # two children, copy the min(cur.right), and remove the min node from right subtree
    elif cur.left != None and cur.right != None:
        # find right subtree's min
        p = cur
        node = cur.right
        while node.left != None:
            p = node
            node = node.left
        cur.val = node.val
        if p == cur:
            cur.right = node.right
        else:
            p.left = node.right

    # one children, remove the node and promote its child
    elif cur.left != None:
        if cur == p.left:
            p.left = cur.left
        else:
            p.right = cur.left
    elif cur.right != None:
        if cur == p.left:
            p.left = cur.right
        else:
            p.right = cur.right
    return dummy.right

def deleteNodeTest():
    root=TreeNode(2)
    root.left=TreeNode(1)
    root.right=TreeNode(4)
    root.right.left=TreeNode(3)
    for i in range(0,8):
        print("remove {}".format(i))
        root=deleteNode(root,i)
        for l in levelOrder(root):
            print(l)
def inorder(root):
    if root==None: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root==None: return []
    result=[]
    q=collections.deque()
    q.append(root)
    while q:
        size=len(q)
        temp=[]
        flag=0
        for i in range(0,size):
            node=q.popleft()
            if node=="#":
                temp.append("#")
                continue
            flag=1
            temp.append(node.val)
            if node.left!=None:
                q.append(node.left)
            else: q.append("#")
            if node.right!=None:
                q.append(node.right)
            else: q.append("#")
        if flag: result.append(temp)
    return result

if __name__ == '__main__':
    readwrite()
    # add comment