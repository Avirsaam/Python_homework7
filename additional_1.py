# 1.Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
#

input_string = "6 12 117 9 36 24 11 99 1"

input_list = list(filter(lambda x: len(x)==2, input_string.split()))
print(input_list)