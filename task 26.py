# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def stepen (a, b):
    count = 1
    if count == b:
        return a

    return a * stepen(a, b - 1)
    

a = int(input("Какое число возводим? "))
b = int(input("А в какую степень? "))
print(f"Число {a} в {b} степени = {stepen(a, b)}")