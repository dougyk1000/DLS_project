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


x_ = np.linspace(0, 2*pi, 16)
fi = [p for p in itertools.product(x_, repeat=4)]


for s in range(1, 65537):

    matrix_iter = str(generate_matrix(fi[s-1]))
    f = open(f'D:\\my_python_projects\\nn_sarov\\best_version\\X_train\\file_matrix{s}.txt', 'w')
    f.write(matrix_iter)
    f1 = open(f'D:\\my_python_projects\\nn_sarov\\best_version\\fi_initial\\fi_initial{s}.txt', 'w')
    f1.write(str(fi[s-1]))
    if s % 655 == 0:
        print(s//655, '%')
    f.close()
    f1.close()
    
print(s)


