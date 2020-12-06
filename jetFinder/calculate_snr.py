import cv2
import numpy as np
from jetFinder import make_plot


def find_signal_of_jet(pic):
    lum_array = list()
    # ----- Different particles -----
    pic = pic[250:340, 1210:1300]
    # pic = pic[260:340, 480:580]
    # pic = pic[280:360, 760:840]

    for _ in range(pic.shape[1]):
        row = list()
        for _ in range(pic.shape[0]):
            row.append(0)
        lum_array.append(row)

    for x in range(pic.shape[1]):
        for y in range(pic.shape[0]):
            b, g, r = pic[y, x]
            lum = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
            lum_array[x][y] = lum

    lum_np_arr = np.array(lum_array)
    max_lum = round(float(np.max(lum_np_arr)), 3)

    return max_lum


def find_noise_near_jet(pic):
    noise_arr = []
    # ----- Different particles -----
    # jets = jets[250:340, 1210:1300]
    # jets = jets[260:340, 480:580]
    pic = pic[340:420, 760:840]

    for _ in range(pic.shape[1]):
        row = list()
        for _ in range(pic.shape[0]):
            row.append(0)
        noise_arr.append(row)

    for x in range(pic.shape[1]):
        for y in range(pic.shape[0]):
            b, g, r = pic[y, x]
            lum = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
            noise_arr[x][y] = lum

    noise_np_array = np.array(noise_arr)
    noise_mean = np.mean(noise_np_array)

    return noise_mean


i = 0
z_array = []
max_lum_array = []

noise_name = "I от Z/Z 0.0425.jpg"
picture = cv2.imread(noise_name)
noise = find_noise_near_jet(picture)
print(noise)

while i != 0.0650:
    i = round(i, 4)

    z_array.append(i)

    name = "I от Z/Z " + str(i) + ".jpg"
    jets = cv2.imread(name)

    max_lum_array.append(find_signal_of_jet(jets))

    i += 0.0025

SNR = np.divide(max_lum_array, noise)
make_plot.make_2d_plot(z_array, SNR)
print(SNR)
