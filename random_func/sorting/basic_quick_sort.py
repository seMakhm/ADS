# ______________________________________________________________________________________________________________________
# quicksort without random pivot
# ______________________________________________________________________________________________________________________
def quicksort(nums, left, right):
    if left < right:
        part_pos = partition(nums, left, right)
        quicksort(nums, left, part_pos - 1)
        quicksort(nums, part_pos - 1, right)


def partition(nums, left, right):
    i = left
    j = right - 1
    pivot = nums[right]

    while i < j:
        while i < right and nums[i] < pivot:
            i += 1
        while j > left and nums[j] >= pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    if nums[i] > pivot:
        nums[i], nums[right] = nums[right], nums[i]

    return i
