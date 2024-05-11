import math
from sympy import diff


def main():
	h_i = [0.1, 0.05, 0.025]
	print("Левые прямоугольники")
	left_rectangles(h_i, 0, 2)
	print("Гаусс")
	euler(h_i, 0, 2)
	print("Эйлер")
	print(0.548 * func(0.225) + 0.902 * func(1) + 0.548 * func(1.7746))
	print(derivative(derivative(derivative(derivative(derivative(derivative(1)))))))


def func(x):
	return math.sin(math.sqrt(1 + x * x))


def derivative(x):
	return diff(func(x))


def left_rectangles(h_i: list, a, b):
	for h in h_i:
		x = a
		integral_val = 0
		m = int((b - a) / h)
		for i in range(m):
			integral_val += (h * func(x))
			x += h
		print(f"for h = {h}, m = {m}, integral value is {integral_val}")


def euler(h_i, a, b):
	for h in h_i:
		m = int((b - a) / h)
		x = a
		integral_val = 0
		integral_val += 0.5 * func(a)
		x += h
		for i in range(1, m):
			integral_val += func(x)
			x += h
		integral_val += 0.5 * func(b)
		integral_val *= h
		integral_val += (1 / 12) * h * h * (derivative(a) - derivative(b))
		print(f"for h = {h}, m = {m}, integral value is {integral_val}")


main()
