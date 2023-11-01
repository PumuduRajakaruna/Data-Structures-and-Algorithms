dataSet = [5, 4, 22, 10, 1, 6, 2, -1]
for i in range(1, len(dataSet)):
    j = i-1
    while j >= 0 and (dataSet[j] > dataSet[j+1]):
        temp = dataSet[j+1]
        dataSet[j+1] = dataSet[j]
        dataSet[j] = temp
        j -= 1
print(dataSet)
