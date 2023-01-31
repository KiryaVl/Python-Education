# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

ticket = int(input("Введите номер билета: "))
first_part  = ticket // 1000
second_part = ticket % 1000
sum1 = 0
sum2 = 0
while first_part > 0 :
    sum1 = sum1 + (first_part % 10)
    first_part //= 10 
while second_part > 0 :
    sum2 = sum2 + (second_part % 10)
    second_part //= 10 
if sum1 == sum2 :
    print(f"YES!, Congratulations! {ticket} it's lucky!")
else :
    print("No, ulucky")