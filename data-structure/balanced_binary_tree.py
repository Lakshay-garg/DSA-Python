# A balanced binary tree, also referred to as a height-balanced binary tree, 
# is defined as a binary tree in which the height of the left and right subtree 
# of any node differ by not more than 1.

# Following are the conditions for a height-balanced binary tree:

# 1. difference between the left and the right subtree for any node is not more than one
# 2. the left subtree is balanced
# 3. the right subtree is balanced

# Checking if a binary tree is height balanced in Python


class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def isBalanced(root):
    def dfs(root):
        if not root:
            return [True,0]
                
        left,right = dfs(root.left),dfs(root.right)
        balanced = (left[0] and right[0] and abs(left[1]-right[1])<=1)
        return [balanced,1+max(left[1],right[1])]
    return dfs(root)[0] 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(isBalanced(root))

# Output = True