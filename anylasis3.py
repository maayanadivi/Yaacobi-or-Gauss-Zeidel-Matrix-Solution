# HomeWork_3
# Maayan Nadivi - 208207068
# Alice Aidlin - 208448326


def main():
    A = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    b = [[2], [6], [5]]
    choise = int(input('Select the desired iterative method:\n1.Jacobi\n2.Gaus Zaidl\n'))
    if choise == 1:
        Jacobi(A, b)
        main()
    elif choise == 2:
        Gauss_Zeidl(A, b)
        main()
    else:
        print('Wrong Choice ! Try again ! ')
        main()


def Dominant_diagonal(matrix):
    if abs(matrix[0][1])+abs(matrix[0][2]) > matrix[0][0]:
        print('There is no dominant diagonal')
        return False
    if abs(matrix[1][0])+abs(matrix[1][2]) > matrix[1][1]:
        print('There is no dominant diagonal')
        return False
    if abs(matrix[2][0])+abs(matrix[2][1]) > matrix[2][2]:
        print('There is no dominant diagonal')
        return False
    return True


def Jacobi(A, b):
    if Dominant_diagonal(A) is True:
        mat = list(range(3))  # make it list
        for i in range(3):
            mat[i] = list(range(1))
        eps = 0.00001
        counter = 0
        x_r = 0
        y_r = 0
        z_r = 0
        mat[0][0] = x_r
        mat[1][0] = y_r
        mat[2][0] = z_r
        print('Iteration {} '.format(counter))
        print(mat)
        counter = counter+1
        x_r1 = (b[0][0] - A[0][1] * y_r - A[0][2] * z_r) / A[0][0]
        y_r1 = (b[1][0] - A[1][0] * x_r - A[1][2] * z_r) / A[1][1]
        z_r1 = (b[2][0] - A[2][0] * x_r - A[2][1] * y_r) / A[2][2]
        mat[0][0] = x_r1
        mat[1][0] = y_r1
        mat[2][0] = z_r1
        print('Iteration {} '.format(counter))
        print(mat)
        while abs(x_r1 - x_r) > eps:

            counter = counter+1
            x_r = x_r1
            y_r = y_r1
            z_r = z_r1
            x_r1 = (b[0][0] - A[0][1] * y_r - A[0][2] * z_r) / A[0][0]
            y_r1 = (b[1][0] - A[1][0] * x_r - A[1][2] * z_r) / A[1][1]
            z_r1 = (b[2][0] - A[2][0] * x_r - A[2][1] * y_r) / A[2][2]

            mat[0][0] = x_r1
            mat[1][0] = y_r1
            mat[2][0] = z_r1
            print('Iteration {} '.format(counter))
            print(mat)


def Gauss_Zeidl(A, b):
    if Dominant_diagonal(A) is True:
        mat = list(range(3))  # make it list
        for i in range(3):
            mat[i] = list(range(1))
        eps = 0.00001
        counter = 0
        x_r = 0
        y_r = 0
        z_r = 0
        mat[0][0] = x_r
        mat[1][0] = y_r
        mat[2][0] = z_r
        print('Iteration {} '.format(counter))
        print(mat)
        counter = counter+1
        x_r1 = (b[0][0] - A[0][1] * y_r - A[0][2] * z_r) / A[0][0]
        y_r1 = (b[1][0] - A[1][0] * x_r1 - A[1][2] * z_r) / A[1][1]
        z_r1 = (b[2][0] - A[2][0] * x_r1 - A[2][1] * y_r1) / A[2][2]
        mat[0][0] = x_r1
        mat[1][0] = y_r1
        mat[2][0] = z_r1
        print('Iteration {} '.format(counter))
        print(mat)
        while abs(x_r1 - x_r) > eps:

            counter = counter+1
            x_r = x_r1
            y_r = y_r1
            z_r = z_r1
            x_r1 = (b[0][0] - A[0][1] * y_r - A[0][2] * z_r) / A[0][0]
            y_r1 = (b[1][0] - A[1][0] * x_r1 - A[1][2] * z_r) / A[1][1]
            z_r1 = (b[2][0] - A[2][0] * x_r1 - A[2][1] * y_r1) / A[2][2]

            mat[0][0] = x_r1
            mat[1][0] = y_r1
            mat[2][0] = z_r1
            print('Iteration {} '.format(counter))
            print(mat)


main()