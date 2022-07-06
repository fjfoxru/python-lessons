def my_func(number_1, number_2, number_3):
    number_list = [number_1, number_2, number_3]
    first_max = max(number_list)
    number_list.remove(first_max)
    second_max = max(number_list)
    print(first_max + second_max)

my_func(70, 50, 20)
