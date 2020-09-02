# write your code here
import numpy as np

value = '_' * 9
value = [elem if elem != '_' else ' ' for elem in value]


def printing():
    print('---------')
    print("| " + value[0] + " " + value[1] + " " + value[2] + " |")
    print("| " + value[3] + " " + value[4] + " " + value[5] + " |")
    print("| " + value[6] + " " + value[7] + " " + value[8] + " |")
    print('---------')


printing()


values = [elem for elem in value]
matrix = [values[i:i+3] for i in range(0, len(values), 3)]


def count_symbol(list_, symbol):
    return list_.count(symbol)


def check_row_win(symbol, matrix=matrix, result=None):
    for elem in matrix:
        if elem.count(symbol) == 3:
            result = symbol
            return result
    return result


def transpose_matrix(matrix=matrix):
    return np.array(matrix).T.tolist()


transpose = transpose_matrix()


def check_col_win(symbol, matrix=transpose, result=None):
    for elem in matrix:
        if elem.count(symbol) == 3:
            result = symbol
            return result
    return result


def check_main_diagonal(symbol, matrix=matrix, result=None):
    diagonal = []
    for i in range(3):
        for j in range(3):
            if i == j:
                diagonal.append(matrix[i][j])
    if diagonal.count(symbol) == 3:
        result = symbol
        return result
    return result


def check_not_main_diagonal(symbol, matrix=matrix, result=None):
    non_diagonal = []
    for i in range(3):
        for j in range(3):
            if j == 3 - i - 1:
                non_diagonal.append(matrix[i][j])
    if non_diagonal.count(symbol) == 3:
        result = symbol
        return result
    return result


def check_winner():
    winner = []
    winner.append(check_row_win('X'))
    winner.append(check_col_win('X'))
    winner.append(check_not_main_diagonal('X'))
    winner.append(check_not_main_diagonal('O'))
    winner.append(check_row_win('O'))
    winner.append(check_col_win('O'))
    winner.append(check_main_diagonal('X'))
    winner.append(check_main_diagonal('O'))
    return winner



counter = 0
while True:
    elem = input('Enter the  coordinates: ')
    elem = elem.replace(' ', '')
    if not elem.isnumeric():
        print('You should enter numbers!')
        continue
    else:
        row = int(elem[0])
        col = int(elem[1])
        i = 3 - col
        j = row - 1

        if (int(elem[0]) < 1) or (int(elem[1]) < 1) or (int(elem[0]) > 3) or (int(elem[1]) > 3):
            print('Coordinates should be from 1 to 3!')
            continue

        elif (matrix[i][j] == 'X') or (matrix[i][j] == 'O'):
            print('This cell is occupied! Choose another one!')
            continue
        else:
            if counter % 2 == 0:
                matrix[i][j] = 'X'
                value = [elem for sublist in matrix for elem in sublist]
                printing()
                counter += 1
            else:
                matrix[i][j] = 'O'
                value = [elem for sublist in matrix for elem in sublist]
                printing()
                counter += 1

        final = list(set(check_winner()))
        if (len(final) == 2) and ('X' in final):
            print('X wins')
            break
        elif (len(final) == 2) and ('O' in final):
            print('O wins')
            break
        if (len(final) == 1) and ('_' not in values) and counter == 9:
            print('Draw')
            break






# values = [elem for elem in value]
# matrix = [values[i:i+3] for i in range(0, len(values), 3)]
#
# print(values)


# def count_symbol(list_, symbol):
#     return list_.count(symbol)
#
#
# def check_row_win(symbol, matrix=matrix, result=None):
#     for elem in matrix:
#         if elem.count(symbol) == 3:
#             result = symbol
#             return result
#     return result
#
#
# def transpose_matrix(matrix=matrix):
#     return np.array(matrix).T.tolist()
#
#
# transpose = transpose_matrix()
#
#
# def check_col_win(symbol, matrix=transpose, result=None):
#     for elem in matrix:
#         if elem.count(symbol) == 3:
#             result = symbol
#             return result
#     return result
#
#
# def check_main_diagonal(symbol, matrix=matrix, result=None):
#     diagonal = []
#     for i in range(3):
#         for j in range(3):
#             if i == j:
#                 diagonal.append(matrix[i][j])
#     if diagonal.count(symbol) == 3:
#         result = symbol
#         return result
#     return result
#
#
# def check_not_main_diagonal(symbol, matrix=matrix, result=None):
#     non_diagonal = []
#     for i in range(3):
#         for j in range(3):
#             if j == 3 - i - 1:
#                 non_diagonal.append(matrix[i][j])
#     if non_diagonal.count(symbol) == 3:
#         result = symbol
#         return  result
#     return result
#
#
# def check_winner():
#     winner = []
#     winner.append(check_row_win('X'))
#     winner.append(check_col_win('X'))
#     winner.append(check_not_main_diagonal('X'))
#     winner.append(check_not_main_diagonal('X'))
#     winner.append(check_row_win('O'))
#     winner.append(check_col_win('O'))
#     winner.append(check_not_main_diagonal('O'))
#     winner.append(check_not_main_diagonal('O'))
#     return winner
#
#
# final = list(set(check_winner()))
#
#
# if (abs(count_symbol(values, 'X') - count_symbol(values, 'O')) >= 2) or len(final) == 3:
#     print('Impossible')
# elif (len(final) == 1) and ('_' in values):
#     print('Game not finished')
# elif (len(final) == 1) and ('_'not in values):
#     print('Draw')
# elif (len(final) == 2) and ('X' in final):
#     print('X wins')
# elif (len(final) == 2) and ('O' in final):
#     print('O wins')

