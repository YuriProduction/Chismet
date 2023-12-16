EPSILON = 0.5 * 10 ** (-4)


def gauss(A, b):
    n = len(A)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j

        A[i], A[max_index] = A[max_index], A[i]
        b[i], b[max_index] = b[max_index], b[i]

        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]
            b[j] -= ratio * b[i]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j] / A[i][i]
    return x


count_iterations_for_Jacobi = 0


def method_Jacobi(x_1, x_2, x_3):
    global count_iterations_for_Jacobi
    count_iterations_for_Jacobi += 1
    x_1_next = (-2.62 + 0.2 * x_2 + 0.31 * x_3) / (-0.6)
    x_2_next = (1.98 + 0.11 * x_3 - 0.2 * x_1) / 1.6
    x_3_next = (2.3 - 0.2 * x_1 + 0.1 * x_2) / 0.9
    if (abs(x_1_next - x_1) < EPSILON
            and abs(x_2_next - x_2) < EPSILON
            and abs(x_3_next - x_3) < EPSILON):
        return x_1_next, x_2_next, x_3_next, count_iterations_for_Jacobi
    return method_Jacobi(x_1_next, x_2_next, x_3_next)


count_iterations_for_Gauss_Zeidel = 0


def method_Gaussa_Zeidelya(x_1, x_2, x_3):
    global count_iterations_for_Gauss_Zeidel
    count_iterations_for_Gauss_Zeidel += 1
    x_1_next = (-2.62 + 0.2 * x_2 + 0.31 * x_3) / (-0.6)
    x_2_next = (1.98 + 0.11 * x_3 - 0.2 * x_1_next) / 1.6
    x_3_next = (2.3 - 0.2 * x_1_next + 0.1 * x_2_next) / 0.9
    if (abs(x_1_next - x_1) < EPSILON
            and abs(x_2_next - x_2) < EPSILON
            and abs(x_3_next - x_3) < EPSILON):
        return x_1_next, x_2_next, x_3_next, count_iterations_for_Gauss_Zeidel
    return method_Gaussa_Zeidelya(x_1_next, x_2_next, x_3_next)


A = [[0.2, 1.6, -0.11], [0.2, -0.1, 0.9], [-0.6, -0.2, -0.31]]
b = [1.98, 2.3, -2.62]
print("Метод Гаусса:", tuple(gauss(A, b)), sep='\n')
print('Метод Якоби', method_Jacobi(4.3666, 1.2374, 2.555), sep='\n')
print('Метод Гаусса-Зейделя', method_Gaussa_Zeidelya(4.3666, 1.2374, 2.555), sep='\n')
