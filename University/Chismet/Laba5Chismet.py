import matplotlib.pyplot as plt
import numpy as np


def exact_func(x):
	return np.log(x + 1) + 3


def exact_solution(x_0, y_0, n, start, end):
	step = (end - start) / n
	x = [x_0]
	y = [y_0]
	cur_x = step
	for i in range(1, n + 1):
		cur_y = exact_func(cur_x)
		x.append(cur_x)
		y.append(cur_y)
		cur_x += step
	return x, y


def Teylor_3(x_0, y_0, n, start, end):
	step = (end - start) / n
	x = [x_0]
	y = [y_0]
	prev_x = x_0
	prev_y = y_0
	for i in range(1, n + 1):
		cur_y = prev_y + step / (prev_x + 1) - step ** 2 / (2 * (prev_x + 1) ** 2) + (2 * step ** 3) / (
				3 * (prev_x + 1) ** 3)
		y.append(cur_y)
		prev_x = prev_x + step
		x.append(prev_x)
		prev_y = cur_y
	return x, y


def Euler(x_0, y_0, n, start, end):
	step = (end - start) / n
	x = [x_0]
	y = [y_0]
	prev_x = x_0
	prev_y = y_0
	for i in range(1, n + 1):
		cur_y = prev_y + 1 / (prev_x + 1) * step
		y.append(cur_y)
		prev_x = prev_x + step
		x.append(prev_x)
		prev_y = cur_y
	return x, y


def Adams_2(x_0, y_0, n, start, end):
	step = (end - start) / n
	x = [x_0]
	y = [y_0]
	prev_x = x_0
	cur_x = prev_x + step
	prev_y = y_0
	for i in range(1, n + 1):
		cur_y = prev_y + step / 2 * (1 / (cur_x + 1) + 1 / (prev_x + 1))
		y.append(cur_y)
		prev_x = cur_x
		cur_x += step
		x.append(prev_x)
		prev_y = cur_y
	return x, y


def visualization_approximation_function(func, title):
	points_count = [5, 10, 20, 30]
	plt.title(title)
	for point_count in points_count:
		res = func(0, 3, point_count, 0, 1)
		x = res[0]
		y = res[1]
		plt.plot(x, y, label=f"Кол-во точек = {point_count}")
	plt.grid(True)
	plt.legend()
	plt.show()


def visualise_all_functions():
	points_count = [10, 20, 30]
	functions = [(exact_solution, "Точное решение"), (Euler, "Эйлер"), (Teylor_3, "Тейлор 3"), (Adams_2, "Трапеций")]
	for point_count in points_count:
		for func in functions:
			res = func[0](0, 3, point_count, 0, 1)
			x = res[0]
			y = res[1]
			plt.plot(x, y, label=f"Метод = {func[1]}")
		plt.title(f"Количество точек = {point_count}")
		plt.grid(True)
		plt.legend()
		plt.show()


def main():
	visualization_approximation_function(exact_solution, "Точное решение")
	visualization_approximation_function(Euler, "Явный метод Эйлера")
	visualization_approximation_function(Teylor_3, "Метод Тейлора 3-го порядка")
	visualization_approximation_function(Adams_2, "Метод трапеций(неявный Адамса 2 порядка)")
	visualise_all_functions()


main()
