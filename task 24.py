# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

bush = int(input("Введите количество кустов: "))
bush_set = list()
bush_sum = list()
for i in range(bush):
    if len(bush_set) < bush:
        bush_set.append(int(input(f"Введите количество ягод на каждом кусте {i+1} : ")))
print(bush_set)
for i in range(len(bush_set) - 1):
    bush_sum.append(bush_set[i - 1] + bush_set[i] + bush_set[i + 1])
bush_sum.append(bush_set[-2] + bush_set[-1] + bush_set[0])
print(max(bush_sum))