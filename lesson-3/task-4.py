def my_func(x, y):
    if type(x) == float and x > 0 and type(y) == int and y < 0:
        return x**y
    else:
        return "Числа не сответствуют условию"

print(my_func(5.1, -7))