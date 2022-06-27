def merge_sort(arr):
    if len(arr) > 1:
        # dividing array
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        # recursion until single element arrays
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merging
        i = 0  # left most element in left array
        j = 0  # right most element in right array
        k = 0  # new array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = right_arr[j]
                k += 1
                j += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
