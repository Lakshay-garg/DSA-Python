def topKFrequent(nums, k):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            
        arr = sorted(d,key=d.get,reverse=True)
        return arr[:k]

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))