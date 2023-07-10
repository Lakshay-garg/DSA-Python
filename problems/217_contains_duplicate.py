# 217. Contains Duplicate
# Given an integer array nums, return true if any 
# value appears at least twice in the array, 
# and return false if every element is distinct.

# For example
# Input: nums = [1,2,3,1]
# Output: true


def ContainDuplicate(nums):
    d = {}
    for i in nums:
        if i in d:
            return True
        else:
            d[i] = 1
    
    return False

nums = [1,2,3,1]
print(ContainDuplicate(nums))

# Output 

# True


    