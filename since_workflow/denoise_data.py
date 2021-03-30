import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size': 18})

dt = 0.001
t = np.arange(-0.5, 0.5, dt)
y = np.sin(2 * np.pi * 50 * t)
# y = np.sin(2 * np.pi * 50 * t)
y_clear = y
y = y + 2.5 * np.random.randn(len(t))

fig, ax = plt.subplots(4, 1)
ax[0].plot(t, y, color='c', linewidth=1.5, label='noisy')
ax[0].plot(t, y_clear, color='k', linewidth=2, label='clean')
ax[0].axis(xmin=t[0], xmax=t[-1])
ax[0].legend()

n = len(t)
f_hat = np.fft.fft(y, n)
AS = np.abs(f_hat) ** 2 / n
# AS = f_hat * np.conj(f_hat) / n
nu_x = (1/dt*n) * np.arange(n)
L = np.arange(1, np.floor(n/2), dtype='int')

ax[1].plot(nu_x[L], AS[L], color='c', linewidth=2)
ax[1].axis(xmin=nu_x[L[0]], xmax=nu_x[L[-1]])

ind = AS > 100
AS_filtered = ind * AS
f_hat = ind * f_hat

ax[2].plot(nu_x[L], AS_filtered[L], color='k', linewidth=2)
ax[2].axis(xmin=nu_x[L[0]], xmax=nu_x[L[-1]])

y_filtered = np.fft.ifft(f_hat)

ax[3].plot(t, y_filtered, color='k', linewidth=2)
ax[3].axis(xmax=t[0], xmin=t[-1])

plt.show()
