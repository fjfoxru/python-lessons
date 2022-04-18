list = []

def sort(a, b):
     sortedList = []
     io = 0
     while io < len(b):
         sortedList.append(b[io])
         sortedList.append(a[io])
         io = io + 1
     return sortedList

while True:
    newElement = input(" элемент")
    list.append(newElement)
    i = 0
    a = []
    b = []
    while i < len(list):
        if (i % 2 == 0):
            a.append(list[i])
        else:
            b.append(list[i])
        i = i + 1
    print(list)
    total = sort(a, b)
    if len(list) % 2 != 0:
        total.append(list[len(list) - 1])
    print(total)