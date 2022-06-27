# ______________________________________________________________________________________________________________________
# bubble sort
# ______________________________________________________________________________________________________________________
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# ______________________________________________________________________________________________________________________
# both ways bubble sort / cocktail shaker sort
# ______________________________________________________________________________________________________________________
def both_ways_bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        c = False
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                c = True
        if not c:
            return nums

        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                c = True
    return nums
