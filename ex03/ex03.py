# Вывести на экран числа от -N до N

print('введите число N')
N = int(input())

if N == 0:
    print('введите N не равное нулю')
else:
    if N > 0:
        nowN = -N
    if N < 0:
        nowN = N
        N = -N
    while nowN <= N:
        print(f' {nowN}')
        nowN += 1
