
#searches for a value and prints the associated key
def searchForValue(searchedItem, myDict):
    for key in myDict.keys():
        if searchedItem in myDict[key]:
            print(key)

#searches for a key and prints out the associated value
def searchForKey(searchedKey, myDict):
    if searchedKey in myDict.keys():
        print(myDict[searchedKey])