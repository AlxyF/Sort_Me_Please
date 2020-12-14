def merge_sort_bottom_up(arr): 
    def merge(arr, arr_c, left, mid, right):
        i = left
        j = mid
        k = left
        while k < right:
            if i < mid and (j >= right or arr_c[i] <= arr_c[j]):
                arr[k] = arr_c[i]
                i += 1
            else:
                arr[k] = arr_c[j]
                j += 1
            k += 1
            yield arr, k - 1
    size = 1
    n = len(arr)
    arr_c = arr.copy()
    while size < n:
        i = 0
        while i < n:
            yield from merge(arr, arr_c, i, min(i + size, n), min(i + 2 * size, n))
            i += 2 * size
        size *= 2
        arr_c = arr.copy()


def merge_sort_top_down(arr, left, right):
    def merge(arr, left, mid, right):
        i = left
        j = mid
        k = left
        arr_c = arr.copy()
        while k < right:
            if i < mid and (j >= right or arr_c[i] <= arr_c[j]):
                arr[k] = arr_c[i]
                i += 1
            else:
                arr[k] = arr_c[j]
                j += 1
            k += 1
            return arr, k - 1

    if (right - left <= 1):
        return
    mid = (left + right)//2

    merge_sort_top_down(arr, left, mid,)
    merge_sort_top_down(arr, mid, right)
    merge(arr, left, mid, right)



