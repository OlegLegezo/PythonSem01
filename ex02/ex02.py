# 2. Найти максимальное из пяти чисел

print('введите число a1')
a1 = int(input())
print('введите число a2')
a2 = int(input())
print('введите число a3')
a3 = int(input())
print('введите число a4')
a4 = int(input())
print('введите число a5')
a5 = int(input())

maximum = a1
if a2>maximum:
    maximum=a2
if a3>maximum:
    maximum=a3
if a4>maximum:
    maximum=a4
if a5>maximum:
    maximum=a5
print(f'максимально из введенных чисел: {maximum}')
