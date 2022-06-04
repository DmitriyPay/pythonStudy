# 1) Сумму ряда 0 - 88888888
from datetime import datetime

t0 = datetime.now()
s = sum(range(0, 88888888))
#print(' Задание 1 --- ',s)
print(datetime.now() - t0, s)

# 2) Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]
arr = [3, 4, 56, 100, 2, 2, 3]
print(' Задание 2 --- ', sum(arr) / len(arr))
       
# 3) Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
s = "asdxfghyxyx"
print(' Задание 3 --- ', s.replace('x', 'y'))

# 4) Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30],
#    кратных и 3 и 5.
arr = [3, 4, 56, 100, 15, 2, 20, 30]
mul = 1
for i in range(0, len(arr)):
    if (arr[i] % 3 == 0 and arr[i] % 5 == 0):
        mul *= arr[i]
print(' Задание 4 --- ', mul)

# 5) Заменить все буквы "x" на "у" в исходной
#    строке без использования дополнительной.
print(' Задание 5 --- ', s.replace('x', 'y'))

#Самостоятельные примеры 

arr = [3, 4, 56, 100, 15, 2, 20, 30]
min = arr.pop(0)
max = min
ind = 0
while arr:
    a = arr.pop(0)
    ind += 1
    if min > a:
        min = a
        ind_min = ind
    if max < a:
        max = a
        ind_max = ind

print(f" MiN = {min}, index min = {ind_min}, MAX = {max}, index max = {ind_max}")

