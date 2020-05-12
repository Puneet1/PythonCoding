def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0]=newList[size-1]
    newList[size-1] = temp
    return newList
newList = [10,12,13,19,20]
print(swapList(newList))