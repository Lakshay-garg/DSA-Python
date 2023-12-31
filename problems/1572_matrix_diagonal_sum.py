# 1572. Matrix Diagonal Sum

# Link to question:- https://leetcode.com/problems/matrix-diagonal-sum/

# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and 
# all the elements on the secondary diagonal that are not part of the primary diagonal.

# For example-->
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

def diagonalSum(mat):
        sum = 0 
        l = len(mat)
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][l-i-1]
        if l%2 ==1:
            sum -= mat[l//2][l//2]
        return sum

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))

# Output
# 25
