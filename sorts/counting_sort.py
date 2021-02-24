

def counting_sort(arr):
    k = max(arr)
    count = [0] * k + [0]
    for x in arr:
        count[x] += 1
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]
    output = [0] * len(arr)
    for x in arr:
        output[count[x]-1] = x
        yield output, count[x]-1
        count[x] -= 1
    yield output, count[x]

#print(counting_sort([1,4,2,3,4,5]))


