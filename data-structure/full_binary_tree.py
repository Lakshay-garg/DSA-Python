# Checking if Binary Tree is a full Binary Tree or not.

# A full Binary tree is a special type of binary tree in which 
# every parent node/internal node has either two or no children.

# It is also known as a proper binary tree.

# Creating a node
class Node:
    def __init__(self,item):
        self.item = item
        self.leftchild = None
        self.rightchild = None

# Checking Full Binary Tree
def isFullBinaryTree(root):
    if root is None:
        return False
    if root.leftchild is None and root.rightchild is None:
        return True
    if root.leftchild is not None and root.rightchild is not None:
        return isFullBinaryTree(root.leftchild) and isFullBinaryTree(root.rightchild)
    return False

root = Node(1)
root.rightchild = Node(3)
root.leftchild = Node(2)

root.leftchild.leftchild = Node(4)
root.leftchild.rightchild = Node(5)
root.leftchild.rightchild.leftchild = Node(6)
root.leftchild.rightchild.rightchild = Node(7)

if isFullBinaryTree(root):
    print("The Tree is a Full Binary Tree")
else:
    print("The Tree is not a Full Binary Tree")

# Output
# The Tree is a Full Binary Tree