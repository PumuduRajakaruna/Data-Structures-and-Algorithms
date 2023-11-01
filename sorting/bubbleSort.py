dataSet = [1,2,4,6,9]
for i in range(len(dataSet)-1):
    flag = 0
    for j in range(len(dataSet)-1-i):
        if dataSet[j] > dataSet[j+1]:
            temp = dataSet[j]
            dataSet[j] = dataSet[j+1]
            dataSet[j+1] = temp
            flag = 1
    if flag == 0:
        break
print(dataSet)


