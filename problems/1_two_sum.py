# 1. Two Sum
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# Link to question:- https://leetcode.com/problems/two-sum/

# For Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def twoSum(nums,target):
        d = {}
        for i,n in enumerate(nums):
            firstnum = target - n
            if firstnum in d:
                return [i,d[firstnum]]
            else:
                d[n] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))

# Output
# [0,1]