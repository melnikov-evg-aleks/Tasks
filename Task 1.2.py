n = input("Введите трехзначное число: ")
n = int(n)
a1 = n % 10
a2 = n % 100 // 10
a3 = n // 100
sum = a1 + a2 + a3
print("Сумма цифр числа", n, ":", sum)