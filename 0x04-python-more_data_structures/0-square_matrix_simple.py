#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    New_matrix = matrix.copy()

    for i in  range(len(matrix)):
        New_matrix[i] = list(map(lambda y:y**2, matrix[i]))

        return(New_matrix)
