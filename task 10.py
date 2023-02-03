# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

head = 0
tail = 0

n = int(input("Введите количество монет: "))
for i in range(n):
    temp = int(input())
    if temp > 0 :
        head += 1
    elif temp == 0 :
        tail += 1
if head > tail:
    print(tail)
else:
    print(head)