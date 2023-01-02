"""
3. Write a python program to compute following computation on matrix:
    a) Addition of two matrices 
    b) Subtraction of two matrices 
    c) Multiplication of two matrices 
    d) Transpose of a matrix  
"""


def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

def addMatrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Martix Cannot be Added! :C"
    else:
        result = [[0 for j in range(len(A[0]))] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] = A[i][j] + B[i][j]

        print("Result of addtion is: ")
        printMatrix(result)
        return result


def subMatrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Martix Cannot be Subtracted! :C"
    else:
        result = [[0 for j in range(len(A[0]))] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] = A[i][j] - B[i][j]

        print("Result of Subtraction is: ")
        printMatrix(result)
        return result


def transpose(matrix):
    # blank matrix creation for result
    result = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

    print("Transpose of the matrix is: ")
    printMatrix(result)
    return result


def multiplyMatrix(mat1, mat2):
    # Condition
    if len(mat1[0]) != len(mat2):
        return "Matrices can't be multiplied"
    else:
        # empty Matrix creation
        result = [[0 for i in range(len(mat1))] for j in range(len(mat2[0]))]
        # multiplication logic
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    result[i][j] += mat1[i][k] * mat2[k][j]

    print("Result Multiplication of Matrix is: ")
    printMatrix(result)
    return result


A = [[1, 4, 5],
     [2, 5, 11],
     [16, 7, 1]]
B = [[0, 9, 0],
     [2, 11, 2],
     [6, 7, 1]]

addMatrix(A, B)
subMatrix(A, B)
multiplyMatrix(A, B)
transpose(A)
transpose(B)
addMatrix(A, B)
