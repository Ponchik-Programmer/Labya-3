# Формируется матрица F следующим образом: если в В количество чисел, меньших К в нечетных столбцах в области 3 больше,
# чем сумма чисел в четных строках в области 2, то поменять в В симметрично области 3 и 2 местами, иначе В и Е поменять
# местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*F– K*AT . Выводятся по
# мере формирования А, F и все матричные операции последовательно.
#                           1
#    E    B            4         2
#    D    C                 3

from random import randint
n = int(input('матрица размером NxN\nвведите N='))
while n < 5:
    print('вы ввели число, не подхлдящие по условие, введите число N, большее или равное 5')
    n = int(input())
k = int(input('число K для сравнения с элементами матрицы \nвведите K='))
print()
print()
print('границы подматриц и областей не включаются')
arr = []
for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(randint(-10, 10))                           #заполнение матрицы А случайными числами от -10 до 10
print('_______________________________________________')
print('A')
for i in range(n):                                                #вывод матрицы А
    for j in range(n):
        print('{:4d}'.format(arr[i][j]), end='')
    print()

frr = []
for i in range(n):                                                #заполнение матрици F элементами матрицы А
    frr.append([])
    for j in range(n):
        frr[i].append(arr[i][j])
print()
print()

a = 0
b = 0
for i in range(n // 2):
    for j in range((n + 1) // 2, n):
        x = i                        #локальные координаты подматрицы В
        y = j - ((n + 1) // 2)
        if (y % 2 == 0) and (x - y > 0) and (x + y > (n // 2) - 1) and (frr[i][j] < k):#условие для 3 области подматрицы B
            a += 1
        if (x % 2 != 0) and (x - y < 0) and (x + y > (n // 2) - 1):#условие для 2 области подматрицы В
            b += frr[i][j]
print('количество чисел A < K в области 3\nA = ', a, '\nсумма чисел B в области 2\nB = ', b)

if a > b:
    print('a > b')
    print('первое условие: поменять в В симметрично области 3 и 2 местами')
    for i in range(((n // 4) + 1),(n // 2)): #смена элементов области 2 и 3 подматрици B
        x = i
        for j in range(((n + 1) // 2) + ((n // 2) - x), (n - ((n // 2) - x))):
            y = j - ((n + 1) // 2)
            frr[y][x + (n // 2)], frr[i][j] = frr[i][j], frr[y][x + (n // 2)]
else:
    print('a <= b')
    print('второе условие: В и Е поменять местами несимметрично')
    for i in range(n // 2):                                   #смена элементов подматриц B и Е
        for j in range(n // 2):
            frr[i][j], frr[i][j + ((n + 1) // 2)] = \
                frr[i][j + ((n + 1) // 2)], frr[i][j]
print('______________________________________________________________________')
print('F')
for i in range(n):                                            #вывод матрици F
    for j in range(n):
        print('{:4d}'.format(frr[i][j]), end='')
    print()
print('______________________________________________________________________')

print('_________________________________________')
print('К * A')
KA = []
for i in range(n):                                             #заготовка для матрицы A умноженную на коиффициент К
    KA.append([])
    for j in range(n):
        KA[i].append(arr[i][j])

for i in range(n):                                             #умножене элементов матриц А на коиффициент К
    for j in range(n):
        KA[i][j] = arr[i][j] * k


for i in range(n):                                             #ввывод матрици равной К * А = КA
    for j in range(n):
        print('{:4d}'.format(KA[i][j]), end='')
    print()

print('_________________________________________')
print('КА * F')

KAF = []                                                        #заготовка под матрицу равной произведению матриц КA и F = KAF
for i in range(n):
    KAF.append([])
    for j in range(n):
        KAF[i].append(frr[i][j])

for i in range(n):
    for j in range(n):
        for h in range(n):
            KAF[i][j] += KA[i][h] * frr[h][j]

for i in range(n):                                              #вывод матрицы KAF
    for j in range(n):
        print('{:4d}'.format(KAF[i][j]), end='')
    print()

tran = []
for i in range(n):                                             #заготовка для транспонентной матрицы Аt
    tran.append([])
    for j in range(n):
        tran[i].append(arr[i][j])

print('___________________________________________')
for i in range(n):                                             #транспонирование матрицы А
    for j in range(n):
        tran[j][i] = arr[i][j]

print('At')                                                    #вывод транспонентной матрици Аt
for i in range(n):
    for j in range(n):
        print('{:4d}'.format(tran[i][j]), end='')
    print()

KAT = []
for i in range(n):                                             #заготовка для транспонентной матрицы Аt
    KAT.append([])
    for j in range(n):
        KAT[i].append(tran[i][j])

for i in range(n):                                             #умножене элементов матриц Аt на коиффициент К
    for j in range(n):
        KAT[i][j] = tran[i][j] * k

print('___________________________________________')
print('KAT')

for i in range(n):                                             #ввывод матрици равной К * Аt = KAT
    for j in range(n):
        print('{:4d}'.format(KAT[i][j]), end='')
    print()

print('___________________________________________')
print('KAF - KAT')

KATF = []
for i in range(n):                                             #заготовка для матрицы равной разницы матриц  KAF - KAT
    KATF.append([])
    for j in range(n):
        KATF[i].append(arr[i][j])

for i in range(n):                                             #вычитание элементов матриц KAF и KAT
    for j in range(n):
        KATF[i][j] = KAF[i][j] - KAT[i][j]

for i in range(n):                                             #ввывод матрици равной выражению ((К*A)*F– K*AT
    for j in range(n):
        print('{:4d}'.format(KATF[i][j]), end='')
    print()
