import numpy as np
from math import pi, exp
import random
import itertools

lmbda = 0.5e-6  # длина волны
k = 2 * pi / lmbda  # Волновое число
z = 4  # Расстояние от XY до UV (Тогда u, v береv в диапазоне [-0.01, 0.01]), чтобы диапазон углов был в [-5, 5]
m = k / z
E0 = 1

x = np.linspace(-0.0009, 0.0009, 20)
y = np.linspace(-0.0009, 0.0009, 20)


def generate_matrix(fi):
    a = 0.003  # Длина стороны
    y20 = 1.05 * a
    x2 = -1.05 * a
    y10 = 0.05 * a
    x1 = -0.05 * a
    y2 = y20
    y1 = y10
    zss = 0
    # xss, yss = 0.001, 0.001
    xss, yss = np.meshgrid(x, y, sparse=True)
    n = 0
    for i in range(2):
        for j in range(2):
            Exy = E0 * (np.cos(fi[n]) + 1j * np.sin(fi[n]))
            zss += (Exy * (
                    np.cos(k * (xss ** 2 + yss ** 2) / (2 * z)) + np.sin(k * (xss * 2 + yss ** 2) / (2 * z)) * 1j) / (
                            1j * lmbda * z) *
                    (-1 / (m * (xss * yss))) * (
                            np.cos((x2 * xss + y2 * yss) * m) - 1j * np.sin((x2 * xss + y2 * yss) * m) -
                            np.cos((x1 * xss + y2 * yss) * m) + 1j * np.sin((x1 * xss + y2 * yss) * m) -
                            np.cos((x2 * xss + y1 * yss) * m) + 1j * np.sin((x2 * xss + y1 * yss) * m) +
                            np.cos((x1 * xss + y1 * yss) * m) - 1j * np.sin((x1 * xss + y1 * yss) * m)))
            n += 1  # Для каждой субаппертуры берем значение из списка fi
            y2 -= 1.1 * a
            y1 -= 1.1 * a
        x2 += 1.1 * a
        x1 += 1.1 * a
        y2 = y20
        y1 = y10
    E = abs(zss) ** 2

    return E


fi = np.random.uniform(-pi, pi, (10001, 4))

for s in range(1, 10001):

    matrix_iter = str(generate_matrix(fi[s-1]))
    f = open(f'D:\\my_pyhton_projects\\nn_sarov\\best_version\\X_validation\\matrix{s}.txt', 'w')
    ff = open(f'D:\\my_pyhton_projects\\nn_sarov\\best_version\\Y_validation\\phases{s}.txt', 'w')
    ff.write(str(fi[s-1]))
    f.write(matrix_iter)
    if s % 100 == 0:
        print(s//100, '%')
    f.close()
    ff.close()
print(s)





