#!/usr/bin/python3
"""
this module contains a function for rotating
a 2D matrix in-place by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix in-place by 90 degrees clockwise.

    Args:
        matrix (list[list]): The 2D matrix to rotate.

    Returns:
        None: The matrix is rotated in-place.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        rotate_2d_matrix(matrix)
        # After rotation:
        # [[7, 4, 1],
        #  [8, 5, 2],
        #  [9, 6, 3]]
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
