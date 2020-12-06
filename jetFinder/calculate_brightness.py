import cv2
import numpy as np
import pylab
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

from mpl_toolkits.mplot3d import Axes3D


def show_me(pic, p_name):
    cv2.imshow(p_name, pic)
    cv2.waitKey()
    cv2.destroyAllWindows()


def save_pic(name_tif, figure):
    png1 = BytesIO()
    figure.savefig(png1, format='png')

    png2 = Image.open(png1)

    png2.save(name_tif + '.tiff')


def signal_to_noise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m / sd)


def make_data(x_range, y_range, lum_arr):
    x = np.array(x_range)
    y = np.array(y_range)
    z = np.array(lum_arr)
    xgrid, ygrid = np.meshgrid(y, x)

    zgrid = z
    return xgrid, ygrid, zgrid


def main():
    i = 0

    z_arr = []
    max_lum_arr = []

    while i != 0.0650:
        i = round(i, 4)
        name = "I от Z/Z " + str(i) + ".jpg"
        z_arr.append(i)
        print(name)
        jets = cv2.imread(name)

        # ----- Different particles -----
        # jets = jets[250:340, 1210:1300]
        # jets = jets[260:340, 480:580]
        jets = jets[280:360, 760:840]
        # lab = cv2.cvtColor(jets, cv2.COLOR_BGR2LAB)

        lum_arr = list()

        for _ in range(jets.shape[1]):
            row = list()
            for _ in range(jets.shape[0]):
                row.append(0)
            lum_arr.append(row)

        for x in range(jets.shape[1]):
            for y in range(jets.shape[0]):
                b, g, r = jets[y, x]
                lum = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
                # print("coordinates of: " + str(x) + " " + str(y) + " are: " + str(r) + " " + str(g) + " " + str(b)
                #       + " and luminance: " + str(lum))
                lum_arr[x][y] = lum

        # show_me(jets, 'lab')

        x_range = []
        y_range = []

        for x in range(jets.shape[1]):
            x_range.append(float(x))

        for y in range(jets.shape[0]):
            y_range.append(float(y))

        x, y, z = make_data(x_range, y_range, lum_arr)

        # ----- Show plots! -----
        fig = pylab.figure()
        axes = Axes3D(fig)

        axes.plot_surface(x, y, z)

        axes.set_xlabel('X coordinate')
        axes.set_ylabel('Y coordinate')
        axes.set_zlabel('Luminance')
        axes.text2D(0, 0.95, "Luminance for Z = " + str(i), transform=axes.transAxes)
        axes.text2D(0, 0.90, "SNR = " + str(round(float(signal_to_noise(jets, axis=None)), 3)),
                    transform=axes.transAxes)
        axes.text2D(0, 0.85, "Max lum = " + str(round(float(np.max(z)), 3)), transform=axes.transAxes)
        pylab.show()
        show_me(jets, 'jets')

        max_lum = round(float(np.max(z)), 3)
        max_lum_arr.append(max_lum)

        # ------ Save pictures! ------
        # d_name = "Lum/" + "I " + str(i)
        # save_pic(d_name, fig)
        # cv2.imwrite('Jet_pic_lum/' + 'JI ' + str(i) + '.jpg', jets)

        i += 0.0025

        cv2.waitKey(0)

    print(z_arr)
    print(max_lum_arr)
    return z_arr, max_lum_arr


if __name__ == '__main__':
    main()
