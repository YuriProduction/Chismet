import numpy as np
from matplotlib import pyplot as plt

epsilon = 10 ** -5
A, B = 0, 1


# аналитическое решение
def analytic_solution(x):
	return np.exp(-x) + np.exp(x) + 3 * x ** 2 - 3 * x - 2


# фи
def phi(y):
	return y - np.e - 1 / np.e + 2


# Тейлор 3-го порядка
def get_by_Euler_Recalculation(x_k, y_k, u_k, h):
	u_ = u_k + h * (y_k + 3 * x_k * (1 - x_k) + 8)
	y_ = y_k + h * u_k
	y_next = y_k + h / 2 * (u_k + u_)
	u_next = u_k + h / 2 * (y_k + 3 * x_k * (1 - x_k) + 8 + y_ + 3 * x_k * (1 - x_k) + 8)
	# y_next = y_k + h * u_k + h ** 2 / 2 * (y_k + 9.8 + 3.9 * x_k * (1 - x_k)) + h ** 3 / 6 * (
	# 		3.9 - 7.8 * x_k + u_k + u_k)
	# u_next = u_k + h * (y_k + 9.8 + 3.9 * x_k * (1 - x_k)) + h ** 2 / 2 * (
	# 		3.9 - 7.8 * x_k + 1 * (y_k + 9.8 + 3.9 * x_k * (1 - x_k))) + h ** 3 / 6 * (
	# 				 -7.8 + 1 * (3.9 - 7.8 * x_k) + 1 * (y_k + 9.8 + 3.9 * x_k * (1 - x_k)))
	return y_next, u_next


# Нахождение значений y
def get_y(mu, N, h):
	y = mu
	u = mu - 3
	all_y = [y]
	for i in range(N):
		y, u = get_by_Euler_Recalculation(h * i, y, u, h)
		all_y.append(y)
	return all_y


# Метод стрельбы
def get_shooting_method(N, mu, mu_0):
	step = 1 / N
	tmp_y = get_y(mu_0, N, step)
	phi_mu_0 = phi(tmp_y[len(tmp_y) - 1])
	tmp_y = get_y(mu, N, step)
	phi_mu = phi(tmp_y[len(tmp_y) - 1])
	while abs(phi_mu) > epsilon:
		tmp_y = get_y(mu, N, step)
		phi_mu = phi(tmp_y[len(tmp_y) - 1])
		mu = mu - phi_mu / (phi_mu - phi_mu_0) * (mu - mu_0)
	print(f'Найденное мю = {mu}')
	return get_y(mu, N, step)


def get_lambda(lambda_i):
	return 1 / (h ** 2 + 2 - lambda_i)


def get_mu(mu, lambda_i, i, h):
	return (mu - h ** 2 * (3.9 * h * i * (1 - h * i) + 9.8)) / (2 + h ** 2 - lambda_i)


# Метод прогонки
def get_tridiagonal_method(h, N):
	all_lambda = []
	all_mu = []
	lambda_i = -1 / (1 + h)
	mu = (-3 * h) / (1 + h)
	all_lambda.append(lambda_i)
	all_mu.append(mu)
	for i in range(1, N + 1):
		tmp = lambda_i
		lambda_i = get_lambda(tmp)
		mu = get_mu(mu, tmp, i, h)
		all_lambda.append(lambda_i)
		all_mu.append(mu)
	length = len(all_lambda)
	all_lambda[length - 1] = 0
	all_mu[length - 1] = np.e + 1 / np.e - 2
	all_y = []
	y = np.e + 1 / np.e - 2
	for k in range(length, 0, -1):
		y = all_lambda[k - 1] * y + all_mu[k - 1]
		all_y.append(y)
	y = list(reversed(all_y))
	return y


# Поиск начальных мю: mu_0 и mu_1
def search_bounds(start=-5):
	while phi(start) < 0:
		start += 1
	return start - 1, start


if __name__ == "__main__":
	Nums = [10, 20]
	for N in Nums:
		h = (B - A) / N
		x = np.linspace(0.0, 1.0, num=N + 1)
		analytic_solutions = [analytic_solution(x_i) for x_i in x]
		mu_0, mu_1 = search_bounds()
		print(f'Для N = {N}')
		print(f'mu_0 = {mu_0}; mu_1 = {mu_1}')
		print(f'phi(mu_0) = {phi(mu_0)}; phi(mu_1) = {phi(mu_1)}')
		
		shooting_y = get_shooting_method(N, mu_0, mu_1)
		tridiagonal_y = get_tridiagonal_method(h, N)
		
		plt.title(f'Для разбиения N={N}')
		plt.plot(x, shooting_y, label="Стрельба")
		plt.plot(x, analytic_solutions, label="Точное решение")
		plt.plot(x, tridiagonal_y, label="Прогонка")
		plt.xlabel('x')
		plt.ylabel('y')
		plt.grid(True)
		plt.legend()
		plt.show()
