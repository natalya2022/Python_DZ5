# 2. Создайте программу для игры в ""Крестики-нолики"".

from functools import reduce


def print_matrix(matrix):       # Функция печати массива
    for i in matrix:
        print(i)


def win(matrix):        # Функция определения победителя
    sum_col = [0, 0, 0]
    sum_diag = 0
    for key, value in enumerate(matrix):        # Выигрыш при заполнении строки, возводим значения в квадрат и складываем
        sum_row = reduce(lambda sum, elem: sum + elem**2, value, 0)
        if sum_row == 3:        # Победил первый (1**2)*3=3
            return 1
        if sum_row == 12:       # Победил второй (2**2)*3=12
            return 2
        for key2, value2 in enumerate(value):      # Считаем столбцы
            sum_col[key2] += value2**2
    for value in sum_col:       # Победил первый (по столбцу)
        if value == 3:
            return 1
        if value == 12:         # Победил второй (по столбцу)
            return 2
    sum_diag = matrix[0][0]**2 + matrix[1][1]**2 + matrix[2][2]**2      # Считаем диагонали
    if sum_diag == 3:
        return 1
    if sum_diag == 12:
        return 2
    sum_diag = matrix[2][0]**2 + matrix[1][1]**2 + matrix[0][2]**2      
    if sum_diag == 3:
        return 1
    if sum_diag == 12:
        return 2
    return 0


matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]      # Задаем массив, заполняем нулями
print_matrix(matrix)

i = 0
while i < 10:
    x, y = map(int, input('Игрок '+str(i % 2+1) + ', ведите позицию строка-столбец через пробел => ').split())
    if y < 0 or y > 2 or x < 0 or x > 2:
        print('Введены данные вне диапазона, введите еще раз ')
        continue
    if matrix[x][y] != 0:
        print('Значение уже введено ранее, введите еще раз ')
        continue
    print(y, x)
    matrix[x][y] = i % 2+1
    i += 1
    print_matrix(matrix)
    test_win = win(matrix)
    if test_win > 0:
        break
print('Выиграл Игрок ', test_win, "\nИгра закончена")
