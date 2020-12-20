'''
Worst-case performance	О(n2) comparisons and  O(n) swaps
Best-case performance	O(n2) comparisons, O(1) swaps
Average performance	О(n2) comparisons and O(n) swaps
Worst-case space complexity	O(1) auxiliary
'''

def selection_sort(arr):
    i = 0
    while i < len(arr):
        min_ = arr[i]
        j = i + 1
        while j < len(arr):
            if arr[j] < min_:
                min_ = arr[j]
                j_m = j
                if i < len(arr) - 1:
                    yield arr, j
            j += 1
        if (arr[i] != min_):
            arr[j_m] = arr[i]
            arr[i] = min_
        i += 1
    yield arr, j - 1

