import math

# погрешность
EPSILON = 0.5 * 10 ** (-5)

# минимальное значение производной
min_derivative = 4.599
max_derivative2 = -0.95533


# значения второй производной
def derivative2_function_value(x: float):
    return -math.cos(x)


# значения производной
def derivative_function_value(x: float):
    return -math.sin(x) - 4.4


# значения функции
def function_value(x: float):
    return math.cos(x) - 4.4 * x


count_dihotomy = 1


# метод дихотомии
def dihotomy(a, b):
    global count_dihotomy
    start_a = a
    start_b = b
    x = None
    while count_dihotomy < math.log2((start_b - start_a) / EPSILON):
        x = (a + b) / 2
        if function_value(a) * function_value(x) < 0:
            b = x
        if function_value(x) * function_value(b) < 0:
            a = x
        count_dihotomy += 1
    return x


count_Newton = 0


def Newton_method(x):
    global count_Newton

    x_next = x - function_value(x) / derivative_function_value(x)
    count_Newton += 1
    if abs(function_value(x_next)) / min_derivative < EPSILON:
        return x_next
    return Newton_method(x_next)


count_Newton_modify = 0


def modyfied_Newton_method(x):
    global count_Newton_modify
    x_next = x - function_value(x) / derivative_function_value(0.3)
    count_Newton_modify += 1
    if abs(function_value(x_next)) / min_derivative < EPSILON:
        return x_next
    return modyfied_Newton_method(x_next)


count_nep_hord = 0


def nepod_hord_method(x):
    global count_nep_hord
    x_next = x - (function_value(x) * (x - 0.3)) / (function_value(x) - function_value(0.3))
    count_nep_hord += 1
    if abs(function_value(x_next)) / min_derivative < EPSILON:
        return x_next
    return nepod_hord_method(x_next)


count_pod_hord = 0


def pod_hord_method(x, x_pred):
    global count_pod_hord
    x_next = x - (function_value(x) * (x - x_pred)) / (function_value(x) - function_value(x_pred))
    count_pod_hord += 1
    if abs(function_value(x_next)) / min_derivative < EPSILON:
        return x_next
    return pod_hord_method(x_next, x)


count_simple_iteration = 0


def simple_iteration_method(x, q, x_0, x_1):
    global count_simple_iteration
    x_next = math.cos(x) / 4.4
    count_simple_iteration += 1
    if q ** count_simple_iteration <= EPSILON * abs(x_0 - x_1) * (1 - q):
        return x_next
    return simple_iteration_method(x_next, q, x_0, x_1)


print('Метод дихотомии')
print(dihotomy(0.2, 0.3))
print(count_dihotomy)
print('Метод Ньютона')
print(Newton_method(0.3))
print(count_Newton)
print('Модифицированный метод Ньютона')
print(modyfied_Newton_method(0.3))
print(count_Newton_modify)
print('Метод неподвижных хорд')
print(nepod_hord_method(0.2))
print(count_nep_hord)
print('Метод подвижных хорд')
print(pod_hord_method(0.3, 0.2))
print(count_pod_hord)
print('Метод простой итерации')
print(simple_iteration_method(0.1 / 2, 0.05484, 0.25, math.cos(0.25) / 4.4))
print(count_simple_iteration)
