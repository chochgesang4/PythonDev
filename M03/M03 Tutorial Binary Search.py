#binarySearch
def binarySearch(listToSearch,thingToSearch):
    length = len(listToSearch)
    
    if (listToSearch[length//2]==thingToSearch):
        return True
    elif(length==1):
        return False
    elif(listToSearch[length//2]>thingToSearch):
        return binarySearch(listToSearch[:(length//2)],thingToSearch)
    else:
        return binarySearch(listToSearch[(length//2):],thingToSearch)


#tests
testList = [1,2,3,4,5,6,7,8,9]

if(binarySearch(testList,5)):
    print("found!")
else:
    print("Not found!")

if(binarySearch(testList,15)):
    print("found!")
else:
    print("Not found!")    