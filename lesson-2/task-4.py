text = input("введите текст")
arrayText = text.split()
i = 0
while i < len(arrayText):
    word = arrayText[i]
    if len(word) < 10:
       print(i + 1, arrayText[i])
    else:
        print(i + 1, arrayText[i][0:10])
    i = i + 1