newList = [2, 'text', 456, 45.3, None]

def checkType(data):
    i = 0
    while len(data) > i:
        print(type(newList[i]))
        i = i + 1

checkType(newList)
