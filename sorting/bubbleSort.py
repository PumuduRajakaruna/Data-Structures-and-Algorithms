dataSet = [1,2,3,4,5,6,10,7,8]
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


