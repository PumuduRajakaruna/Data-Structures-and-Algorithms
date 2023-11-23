# Quick sort : Iterative method
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [], greater = []
        for x in arr[1:]:
            if x <= pivot:
                less.append(x)
            else:
                greater.append(x)

        return quick_sort(less) + [pivot] + quick_sort(greater)
