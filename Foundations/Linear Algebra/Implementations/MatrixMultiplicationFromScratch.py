import numpy as np

print("Matrix calculator for 3x3 matrices")

vector1i = [int(input("Enter matrix 1: ")), int(input()), int(input())]
vector1j = [int(input()), int(input()), int(input())]
vector1k = [int(input()), int(input()), int(input())]
print()
vector2i = [int(input("Enter matrix 2: ")), int(input()), int(input())]
vector2j = [int(input()), int(input()), int(input())]
vector2k = [int(input()), int(input()), int(input())]
print()
matrix1 = [vector1i, vector1j, vector1k]
matrix2 = [vector2i, vector2j, vector2k]

vector3i = [0, 0, 0]
vector3j = [0, 0, 0]
vector3k = [0, 0, 0]

for i in range(0, 3):
    vector3i[i] = (
        (vector2i[i] * vector1i[0])
        + (vector2j[i] * vector1i[1])
        + (vector2k[i] * vector1i[2])
    )
    vector3j[i] = (
        (vector2i[i] * vector1j[0])
        + (vector2j[i] * vector1j[1])
        + (vector2k[i] * vector1j[2])
    )
    vector3k[i] = (
        (vector2i[i] * vector1k[0])
        + (vector2j[i] * vector1k[1])
        + (vector2k[i] * vector1k[2])
    )

matrix3 = np.array([vector3i, vector3j, vector3k]).T
print("Raw Python result: ", end="")
print(matrix3)

"""
NUMPY METHOD
"""


cols1 = [vector1i, vector1j, vector1k]
A = np.array(cols1).T
cols2 = [vector2i, vector2j, vector2k]
B = np.array(cols2).T
print("Numpy result: ", (B @ A))
