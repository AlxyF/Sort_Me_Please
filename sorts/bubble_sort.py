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
