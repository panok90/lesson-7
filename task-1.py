"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.


Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        self.str_matrix = '\n'.join(['\t'.join([str(row) for row in line]) for line in self.args])
        return self.str_matrix

    def __add__(self, other):
        result = list()
        list_in = list()
        for line in range(len(self.args)):
            for row in range(len(self.args[line])):
                sum_result = self.args[line][row] + other.args[line][row]
                list_in.append(sum_result)
            result.append(list_in)
            list_in = []
        return Matrix(result)


matrix1_3x2 = [[31, 32], [37, 43], [51, 86]]
matrix2_3x2 = [[3, 3], [3, 4], [5, 8]]
matrix1 = Matrix(matrix1_3x2)
matrix2 = Matrix(matrix2_3x2)
print(matrix1 + matrix2)
