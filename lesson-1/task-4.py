n = input("положительное число")
numbers = list(str(n))
result = 0
i = 0
while i < len(numbers):
    if result < int(numbers[i]):
        result = int(numbers[i])
    i = i + 1

print(result)