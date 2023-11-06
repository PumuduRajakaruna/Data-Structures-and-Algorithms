dataSet = [7, 6, 10, 5, 9, 2, 1, 15, 7]


def position(dataSet, lb, ub):
    pivot = dataSet[lb]
    start = lb
    end = ub
    while start < end:
        while dataSet[start] <= pivot:
            start += 1
        while dataSet[end] > pivot:
            end -= 1
        if start < end:
            temp = dataSet[start]
            dataSet[start] = dataSet[end]
            dataSet[end] = temp
    temp = dataSet[lb]
    dataSet[lb] = dataSet[ub]
    dataSet[ub] = temp
    return end


def quickSort(dataSet, lb, ub):
    if lb < ub:
        loc = position(dataSet, lb, ub)
        quickSort(dataSet, lb, loc - 1)
        quickSort(dataSet, loc + 1, ub)
    print(dataSet)

quickSort(dataSet,7,7)