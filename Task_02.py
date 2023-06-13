# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n = 10
list = []
for i in range(n):
    list.append(randint(1, 10))
list_1 = []
min = 3
max = 8
for i in range(len(list)):
    if min < list[i] < max:
        list_1.append((i, list[i]))

print(list)
print(list_1)
