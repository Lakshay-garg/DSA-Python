# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return 
# the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# For example
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.

# Link to question:- https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
        nums = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in nums:
                length = 0
                while (i+length) in nums:
                    length += 1
                longest = max(length,longest)

        return longest

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))

# Output
# 4
