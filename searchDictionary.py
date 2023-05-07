#searches a dictionary, takes a specified value, and a dictionary. Optionally can also take a key to reduce search time. 

def searchDict(searchedItem, myDict):
    for key in myDict.keys():
        if searchedItem in myDict[key]:
            print(key)
