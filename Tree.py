import pickle
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root == None: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root == None: return []
    result = []
    q = collections.deque()
    q.append(root)
    while q:
        size = len(q)
        temp = []
        flag = 0
        for i in range(0, size):
            node = q.popleft()
            if node == "#":
                temp.append("#")
                continue
            flag = 1
            temp.append(node.val)
            if node.left != None:
                q.append(node.left)
            else:
                q.append("#")
            if node.right != None:
                q.append(node.right)
            else:
                q.append("#")
        if flag: result.append(temp)
    return result


if __name__ == '__main__':
    print(1)
# add comment
