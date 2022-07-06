def calc_numbers(total_sum = 0):
    user_numbers = input("Введите числа, разделитель: пробел")
    number_list = user_numbers.split(" ")
    local_list = []
    i = 0
    while i < len(number_list):
        try:
            value = int(number_list[i])
            local_list.append(value)
        except Exception:
            print("Неправильное число")
            break;

        i = i + 1
    total_sum_local = total_sum + sum(local_list)
    print(f"Сумма: {total_sum_local}")
    calc_numbers(total_sum_local)

calc_numbers()
