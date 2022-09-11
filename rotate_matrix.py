#rotate a matrix in place

def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j], matrix[j][i]= matrix[j][i],matrix[i][j]
    return matrix

def reverseRows(matrix):
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix

def displayMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], " ", end='')
        print()


if __name__ == "__main__":
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    displayMatrix(matrix)
    transpose(matrix)
    reverseRows(matrix)
    displayMatrix(matrix)
