# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите число: "))
count = 0
sum = 0
z = 0
while count < 3 :
    z = number % 10 
    sum = sum + z
    number = number // 10
    count = count + 1

print(sum)