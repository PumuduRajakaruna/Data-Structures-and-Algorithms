dataSet = [7, 6, 10, 5, 9, 2, 1, 15, 7]

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

sorted_list = quickSort(dataSet)
print(sorted_list)
