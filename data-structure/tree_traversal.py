# Tree Traversal Notes and It's Type with implementation

# Traversing a tree means visiting every node in the tree. 
# You might, for instance, want to add all the values in the 
# tree or find the largest one. For all these operations, 
# you will need to visit each node of the tree.

# There are 3 types of Traversal
# 1. Inorder (left,root,right) (To learn we can think From In in Inorder that root is in between)
# 2. Preorder (root,left,right) (To learn we can think From Pre in Preorder that root is at first place)
# 3. Postorder (left,right,root) (To learn we can think From Post in Postorder that root is at last place) 

# Tree Traversal Code

class Node:
    def __init__(self,item):
        self.right = self.left = None
        self.val = item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "-->",end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(str(root.val) + "-->",end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "-->",end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)

# Output

# Inorder traversal 
# 4--> 2--> 5--> 1--> 3-->

# Preorder traversal
# 1--> 2--> 4--> 5--> 3-->

# Postorder traversal
# 4--> 5--> 2--> 3--> 1-->
