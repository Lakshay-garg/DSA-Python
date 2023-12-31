# 1512. Number of Good Pairs

# Link to question:- https://leetcode.com/problems/number-of-good-pairs/

# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

def numIdenticalPairs(nums):
        count = 0
        d = {}
        for i in nums:
            if i in d:
                count += d[i]
                d[i] += 1
            else:
                d[i] = 1
        return count

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))

# Output
# 4