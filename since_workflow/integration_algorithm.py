import matplotlib.pyplot as plt
import numpy as np


def nm2m(nm):
    return nm * 1e-9


def px2m(px, px_size_m=5.04e-6):
    return px * px_size_m


def um2m(um):
    return um * 1e-6


def mm2m(mm):
    return mm * 1e-3


def gauss_1d(x, a=1., w=1., x0=0.):
    return a * np.exp(-(x - x0) ** 2 / (2 * w ** 2))


def rect_1d(x, a=1., w=1., x0=0.):
    return a * (np.abs((x - x0) / w) < 0.5)


def rayleigh_sommerfeld_multiplier():
    return (z * np.exp(1j * k * r)) / (np.sqrt(r ** 3) * 1j * np.sqrt(wavelength))


def rectangle_rule(field, a, b, nseg=512, frac=0.5):
    dx = (b - a) / nseg
    summa = 0
    x_start = a + frac * dx
    for i in range(nseg):
        cur = field[i] * dx
        summa += cur

    return summa


# Параметры оптической системы
height = 512
wavelength = nm2m(659.6)
w = px2m(250)
focal_len = 100
px_size = um2m(5.04)
k = 2 * np.pi / wavelength

# Координата перемещения волны
z = 150
z = mm2m(z)

# Задаю сетку по X
X = np.arange(-height / 2, height / 2)
# Перевожу пиесели в метры
X = px2m(X)
# Нахожу интенсивность в z = 0
intensity = gauss_1d(X, w=w / 4, x0=np.average(X))

# Задание апертуры
aperture = rect_1d(X, w=2 * w, x0=np.average(X))
# Сходящаяся сферическая волна
radius_vector = np.sqrt(X ** 2 + mm2m(focal_len) ** 2)
# g(x, 0)
g0 = np.sqrt(intensity) * np.exp(-1j * k * radius_vector) * aperture

# Завожу массив нулей под g(x, z)
gZ = np.zeros(g0.shape, dtype=complex)

for g_, x_ in enumerate(X):
    r = np.sqrt((X - x_) ** 2 + z ** 2)  # расчёт r'
    multiplier = rayleigh_sommerfeld_multiplier()  # расчёт множителя под интегралом RS
    result = multiplier * g0  # значение подинетгрального выражения
    one_sum = rectangle_rule(result, X[0], X[-1], X.shape[0])
    gZ[g_] = one_sum

# plt.plot(X, gZ)
# plt.title(f'RS : {z} m')
# plt.show()
