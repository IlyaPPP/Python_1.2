# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в
# массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите количетсво чисел: "))
list_1 = [int(input("Введите число: ")) for i in range(n)]
print(*list_1)

x = int(input("Введите x: "))
list_1.append(x)
min_diff = 100
low_position = 0
high_position = 0
for i in range(n+1):
    if list_1[-1] > list_1[i] and list_1[-1] - list_1[i] <= min_diff:
        min_diff = list_1[-1] - list_1[i]
        low_position = list_1[i]
    elif list_1[-1] < list_1[i] and list_1[i] - list_1[-1] <= min_diff:
        min_diff = list_1[i] - list_1[-1]
        high_position = list_1[i]

if low_position != 0:
    print(low_position)
if high_position != 0:
    print(high_position)