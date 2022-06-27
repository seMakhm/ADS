# ______________________________________________________________________________________________________________________
# merge sort without slicing
# ______________________________________________________________________________________________________________________
def merge_sort_without_slicing(nums):
    f = len(nums)
    if f > 1:
        # dividing array
        h = f // 2
        left_arr = []
        right_arr = []
        for i in range(h):
            left_arr.append(nums[i])
        for i in range(h, f, 1):
            right_arr.append(nums[i])

        # recursion until single element arrays
        merge_sort_without_slicing(left_arr)
        merge_sort_without_slicing(right_arr)

        # merging
        i = 0  # left most element in left array
        j = 0  # right most element in right array
        k = 0  # new array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                nums[k] = left_arr[i]
                k += 1
                i += 1
            else:
                nums[k] = right_arr[j]
                k += 1
                j += 1

        # checking if anything left in lists
        while i < len(left_arr):
            nums[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            nums[k] = right_arr[j]
            j += 1
            k += 1
