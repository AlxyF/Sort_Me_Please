'''
Worst-case performance	О(n2) comparisons and swaps
Best-case performance	O(n) comparisons, O(1) swaps
Average performance	О(n2) comparisons and swaps
Worst-case space complexity	О(1) total, O(1) auxiliary
'''


def bubble_sort(arr):
    swapped = True
    ranged = len(arr)
    while swapped is not False:
        i = 1
        swapped = False
        while i < ranged:
            checking = i - 1
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
            yield (arr, checking)
            i += 1
        ranged -= 1
