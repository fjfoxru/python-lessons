def division_numbers(number_1, number_2):
    if (number_1 == 0 or number_2 == 0):
        print("Делить ноль или на ноль нельзя")
    else:
        print(number_1 / number_2)


number1 = int(input("Первое число"))
number2 = int(input("Второе число"))


division_numbers(number1, number2)
