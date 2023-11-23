# arr is the array
# t is the target that we need to find the index
# in this code initial pivot get as the first element of the array
# reason behind using while low <= high: (in line 9)
# because if we use while low < high: without the equal sign last element going to be missed
# loop will truncate before checking the last element
def bin_search(arr, t):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if t == arr[mid]:
            return mid
        elif t > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None
