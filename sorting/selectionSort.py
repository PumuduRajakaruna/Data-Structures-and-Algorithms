dataSet = [1,2,3,4,5,6,10,7,8]

for i in range(len(dataSet)):
    min = dataSet[i]
    for j in range(i, len(dataSet)):
        if dataSet[j] < min:
            min = dataSet[j]
    dataSet[dataSet.index(min)] = dataSet[i]
    dataSet[i] = min
print(dataSet)
