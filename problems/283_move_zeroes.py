def move_zeroes(nums):
    l = 0
    r = 1
    while r < len(nums):
        if nums[l] != 0 and nums[r] == 0:
            l = r
            r += 1
        elif nums[l] == 0 and nums[r] != 0:
            nums[l],nums[r] = nums[r],nums[l]
            r += 1
            l +=1
        else:
            r += 1
    return nums