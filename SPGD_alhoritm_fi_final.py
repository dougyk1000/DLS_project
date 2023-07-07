import numpy as np
from math import pi, exp
import random
import itertools

lmbda = 0.5e-6  # длина волны
k = 2 * pi / lmbda  # Волновое число
z = 4  # Расстояние от XY до UV (Тогда u, v береv в диапазоне [-0.01, 0.01]), чтобы диапазон углов был в [-5, 5]
m = k / z
E0 = 1

def I_0(fi, zss=0, a=0.003):
    for i in range(4):
        zss += E0 / (1j * lmbda * z) * (a ** 2) * (np.cos(fi[i]) + 1j * np.sin(fi[i]))
    E = abs(zss) ** 2
    return E


x_ = np.linspace(0, 2*pi, 16)
fi = [p for p in itertools.product(x_, repeat=4)]
lr = 3
for f in range(1, 65537):
    if f % 1000 == 0:
        print(f/65536*100, '%')
    for i in range(40):
        delta = [-0.03, 0.03]
        dfi = []
        for j in range(4):
            dfi.append(random.choice(delta))
        dfi = np.array(dfi)
        if I_0(fi[f-1] + dfi) > I_0(fi[f-1]):
            b = 1
        else:
            b = -1
        fi[f-1] = fi[f-1] + lr * b * dfi

    file1 = open(f'D:\\my_pyhton_projects\\nn_sarov\\best_version\\fi_finished\\fi_finished{f}.txt', 'w')
    file1.write(str(fi[f-1]))
    file1.close()
