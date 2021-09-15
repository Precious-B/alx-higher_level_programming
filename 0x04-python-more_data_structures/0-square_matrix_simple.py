#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for a in matrix:
        squared_matrix.append([b ** 2 for b in a])
    return squared_matrix
