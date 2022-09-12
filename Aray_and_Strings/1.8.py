#Zero Matrix

l = [[1,2,3,0,5],
     [1,2,3,4,5],
     [0,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,0],
     [1,2,3,4,5]]


def print_mat(l):
    for i in l:
        for j in i:
            print(j,end="   ")
        print("\n")



def zero_matrix(l):
    rowzero = 0 
    colzero = 0
    m = len(l)
    n = len(l[0])
    for i in range(m):
        if l[i][0] == 0:
            rowzero = 1

    for i in range(n):
        if l[0][i] == 0:
            colzero = 1
    
    for i in range(1,m):
        for j in range(1,n):
            if l[i][j] == 0:
                l[i][0] = 0
                l[0][j] = 0

    for i in range(1,m):
        if l[i][0] == 0:

            for j in range(1,n):
                l[i][j] = 0

    for i in range(1,n):
        if l[0][i] == 0:
            for j in range(1,m):
                l[j][i] = 0

    if rowzero == 1:
        for i in range(n):
            l[0][i] = 0

    if colzero == 1:
        for i in range(m):
            l[i][0] = 0

    print_mat(l)


zero_matrix(l)

