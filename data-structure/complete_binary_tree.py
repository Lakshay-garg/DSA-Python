# Complete Binary Tree

# A complete binary tree is a binary tree in which all the levels are completely 
# filled except possibly the lowest one, which is filled from the left.

# A complete binary tree is just like a full binary tree, but with two major differences

# 1. All the leaf elements must lean towards the left.
# 2. The last leaf element might not have a right sibling i.e. a complete binary tree doesn't 
# have to be a full binary tree.

# Creating Node
class Node:
    def __init__(self,val):
        self.left = self.right = None
        self.val = val

# Counting Nodes
def countnodes(root):
    if root is None:
        return 0
    return (1+ countnodes(root.left) + countnodes(root.right))

def iscomplete(root,index,nodecount):
    if root is None:
        return True
    if index >= nodecount:
        return False
    return (iscomplete(root.left,2*index+1,nodecount) + iscomplete(root.right,2*index+2,nodecount))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

number_node = countnodes(root)
index = 0

if iscomplete(root,index,number_node):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")

# Output
# The tree is a complete binary tree