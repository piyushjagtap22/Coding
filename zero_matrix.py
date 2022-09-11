def ZeroMatrix(matrix):
    rowHasZero = False
    columnHasZero = False

    for j in range(len(matrix)):
        if matrix[0][j] == 0:
            rowHasZero = True
            break
    
    for j in range(len(matrix)):
        if matrix[j][0] == 0:
            columnHasZero = True
            break

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(len(matrix)):
        if matrix[i][0] == 0 :
            matrix = nullifyRows(matrix,i)

    for j in range(len(matrix)):
        if matrix[0][j] == 0 :
            matrix = nullifyColumn(matrix,j)

    if rowHasZero : nullifyRows(matrix,0)
    if columnHasZero : nullifyColumn(matrix,0)
         
    return matrix


def nullifyColumn(matrix,j):
    for i in range(len(matrix)):
        matrix[i][j] = 0
    return matrix

def nullifyRows(matrix,i):
    for j in range(len(matrix[0])):
        matrix[i][j] = 0
    return matrix

def displayMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], " ", end='')
        print()

if __name__ == "__main__":
    matrix = [[1,1,3],
              [2,5,6],
              [7,8,0]]

    displayMatrix(matrix)
    ZeroMatrix(matrix)
    print('------')
    displayMatrix(matrix)
