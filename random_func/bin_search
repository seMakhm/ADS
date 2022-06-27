def bin_search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + ((r - l) // 2)
        # if target == nums[l]:
        #     return l
        # if target == nums[r]:
        #     return r
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            return m
    return -1
