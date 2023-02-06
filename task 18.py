# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

from array import *

a = []
n = int(input("Введите число: "))
for i in range(n):
    a.append(int(input()))
print(a)
a.sort()
x = int(input("Какое число ищем? "))
count = x
result = a[0]
for i in a:
    if abs(i - x) < count:
        count = abs(i - x)
        result = i
print("x = ", result)
    
