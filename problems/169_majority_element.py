def majority(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    n = len(nums)
    for i in d:
        if d[i] > n//2:
            return i

nums = [3,2,3]
print(majority(nums))