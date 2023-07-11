# Checking if a binary tree is a perfect binary tree in Python

# A perfect binary tree is a type of binary tree in which every 
# internal node has exactly two child nodes and all the leaf nodes 
# are at the same level.

# All the internal nodes have a degree of 2.

# Recursively, a perfect binary tree can be defined as:

# 1. If a single node has no children, it is a perfect binary tree of height h = 0,
# 2. If a node has h > 0, it is a perfect binary tree if both of its subtrees are of 
#    height h - 1 and are non-overlapping.

# Creating a node
class newNode:
    def __init__(self,item):
        self.item = item
        self.left = self.right = None

# Calculate the Depth 

def calculate_Depth(node):
    d= 0 
    while node is not None:
        d += 1
        node = node.left
    return d

def perfect_Binary_tree(node,d,level=0):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return (d==level+1)
    if node.left is None or node.right is None:
        return False
    return (perfect_Binary_tree(node.left,d,level+1) and perfect_Binary_tree(node.right,d,level+1))

# Input For a perfect Binary Tree

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
if perfect_Binary_tree(root,calculate_Depth(root)):
    print("It is a perfect binary Tree")
else:
    print("It is not a perfect binary tree")

# Output 
# It is a perfect binary Tree

#-----------------------------------------------#

# Input For not a perfect Binary Tree

# root = newNode(1)
# root.left = newNode(2)
# root.right = newNode(3)
# root.left.left = newNode(4)
# root.left.right = newNode(5)
# if perfect_Binary_tree(root,calculate_Depth(root)):
#     print("It is a perfect binary Tree")
# else:
#     print("It is not a perfect binary tree")

# Output 
# It is not a perfect binary Tree