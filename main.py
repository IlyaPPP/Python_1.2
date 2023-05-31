# Задача N°23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

array = []

print("Введите 5 чисел")

for x in range(5): array.append(int(input("Введите число: ")))

count = 0
array_2 = []
for i in range(4):
    if array[i+1] > array[i]:
        count+=1
        array_2.append(array[i])
        array_2.append("<")
        array_2.append(array[i+1])
        array_2.append(",")
print(count), print(*array_2)