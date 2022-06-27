# ______________________________________________________________________________________________________________________
# in place merge sort with Time O(n log(n)) and Space O(1)
# ______________________________________________________________________________________________________________________
def sort_imerge(Nums, l=0, u=None):
    # u = len(Seq) if u is None else u
    u = len(Nums)
    if u - l > 1:
        m = l + (u - l) // 2
        w = l + u - m
        wsort(Nums, l, m, w)
        while w - l > 2:
            n = w
            w = l + (n - l + 1) // 2
            wsort(Nums, w, n, l)
            wmerge(Nums, l, l + n - w, n, u, w)
        n = w
        while n > l:  # fallback to insert sort
            for m in range(n, u):
                if Nums[m - 1] > Nums[m]:
                    Nums[m - 1], Nums[m] = Nums[m], Nums[m - 1]
            n -= 1


def wmerge(Nums, i, m, j, n, w):
    while i < m and j < n:
        if Nums[i] < Nums[j]:
            Nums[i], Nums[w] = Nums[w], Nums[i]
            i += 1
        else:
            Nums[j], Nums[w] = Nums[w], Nums[j]
            j += 1
        w += 1
    while i < m:
        Nums[i], Nums[w] = Nums[w], Nums[i]
        i += 1
        w += 1
    while j < n:
        Nums[j], Nums[w] = Nums[w], Nums[j]
        j += 1
        w += 1


def wsort(Nums, l, u, w):
    if u - l > 1:
        m = l + (u - l) // 2
        sort_imerge(Nums, l, m)
        sort_imerge(Nums, m, u)
        wmerge(Nums, l, m, m, u, w)
    else:
        while l < u:
            Nums[l], Nums[w] = Nums[w], Nums[l]
            l += 1
            w += 1
