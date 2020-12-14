'''
Worst-case performance	О(n2) comparisons and swaps
Best-case performance	O(n) comparisons, O(1) swaps
Average performance	О(n2) comparisons and swaps
Worst-case space complexity	О(n) total, O(1) auxiliary
'''


def insertion_sort(arr):
    i = 1
    while i < len(arr):
        x = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr, j

        arr[j + 1] = x
        i += 1
