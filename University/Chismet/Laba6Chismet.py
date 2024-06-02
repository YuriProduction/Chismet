import numpy as np
import matplotlib.pyplot as plt

epsilon = 1e-5
LEFT, RIGHT = 0, 1


def analytic_solution(x):
	return np.exp(-x) + np.exp(x) + 3 * x ** 2 - 3 * x - 2


def phi(y):
	return y - np.e - 1 / np.e + 2


def Euler_Recalculation(x_k, y_k, u_k, h):
	u_ = u_k + h * (y_k + 3 * x_k * (1 - x_k) + 8)
	y_ = y_k + h * u_k
	y_next = y_k + h / 2 * (u_k + u_)
	u_next = u_k + h / 2 * (y_k + 3 * x_k * (1 - x_k) + 8 + y_ + 3 * x_k * (1 - x_k) + 8)
	return y_next, u_next


def Y(mu, N, h):
	y = mu
	u = mu - 3
	all_y = [y]
	for i in range(N):
		y, u = Euler_Recalculation(h * i, y, u, h)
		all_y.append(y)
	return all_y


def Shooting(N, mu, mu_0):
	step = 1 / N
	tmp_y = Y(mu_0, N, step)
	phi_mu_0 = phi(tmp_y[-1])
	tmp_y = Y(mu, N, step)
	phi_mu = phi(tmp_y[-1])
	while abs(phi_mu) > epsilon:
		tmp_y = Y(mu, N, step)
		phi_mu = phi(tmp_y[-1])
		mu = mu - phi_mu / (phi_mu - phi_mu_0) * (mu - mu_0)
	return Y(mu, N, step)


def Lambda(lambda_i, h):
	return 1 / (h ** 2 + 2 - lambda_i)


def Mu(mu, lambda_i, i, h):
	return (mu - h ** 2 * (3.9 * h * i * (1 - h * i) + 9.8)) / (2 + h ** 2 - lambda_i)


def Progonka(h, N):
	all_lambda = []
	all_mu = []
	lambda_i = -1 / (1 + h)
	mu = (-3 * h) / (1 + h)
	all_lambda.append(lambda_i)
	all_mu.append(mu)
	for i in range(1, N + 1):
		tmp = lambda_i
		lambda_i = Lambda(tmp, h)
		mu = Mu(mu, tmp, i, h)
		all_lambda.append(lambda_i)
		all_mu.append(mu)
	length = len(all_lambda)
	all_lambda[-1] = 0
	all_mu[-1] = np.e + 1 / np.e - 2
	all_y = []
	y = np.e + 1 / np.e - 2
	for k in range(length, 0, -1):
		y = all_lambda[k - 1] * y + all_mu[k - 1]
		all_y.append(y)
	y = list(reversed(all_y))
	return y


def find_start_mu(start=-5):
	while phi(start) < 0:
		start += 1
	return start - 1, start


if __name__ == "__main__":
	Nums = [10, 20]
	for N in Nums:
		h = (RIGHT - LEFT) / N
		x = np.linspace(LEFT, RIGHT, num=N + 1)
		analytic_solutions = analytic_solution(x)
		mu_0, mu_1 = find_start_mu()
		shooting_y = Shooting(N, mu_0, mu_1)
		tridiagonal_y = Progonka(h, N)
		
		plt.title(f'N={N}')
		plt.plot(x, shooting_y, label="Стрельба")
		plt.plot(x, analytic_solutions, label="Точное решение")
		plt.plot(x, tridiagonal_y, label="Прогонка")
		plt.xlabel('x')
		plt.ylabel('y')
		plt.grid(True)
		plt.legend()
		plt.show()
