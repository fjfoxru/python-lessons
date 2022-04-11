a = int(input( "1  день"))
b = int(input(" желаемый результат"))

day = 1
result: int = a
while result < b:
    result = result + ((result / 100) *10)
    day = day + 1
print(day)