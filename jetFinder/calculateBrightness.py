import cv2
import numpy as np
import pylab
from io import BytesIO
from PIL import Image

from mpl_toolkits.mplot3d import Axes3D


def show_me(pic, name):
    cv2.imshow(name, pic)
    cv2.waitKey()
    cv2.destroyAllWindows()


def save_pic(name_tif):
    png1 = BytesIO()
    fig.savefig(png1, format='png')

    png2 = Image.open(png1)

    png2.save(name_tif + '.tiff')


i = 0

while i != 0.0650:
    i = round(i, 4)
    name = "I от Z/Z " + str(i) + ".jpg"
    print(name)
    jets = cv2.imread(name)
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
            print("coordinates of: " + str(x) + " " + str(y) + " are: " + str(r) + " " + str(g) + " " + str(b)
                  + " and luminance: " + str(lum))
            lum_arr[x][y] = lum

    # show_me(jets, 'lab')

    x_range = []
    y_range = []

    for x in range(jets.shape[1]):
        x_range.append(float(x))

    for y in range(jets.shape[0]):
        y_range.append(float(y))


    def makeData():
        x = np.array(x_range)
        y = np.array(y_range)
        z = np.array(lum_arr)
        xgrid, ygrid = np.meshgrid(y, x)

        zgrid = z
        return xgrid, ygrid, zgrid


    x, y, z = makeData()

    fig = pylab.figure()
    axes = Axes3D(fig)

    axes.plot_surface(x, y, z)

    pylab.show()

    show_me(jets, 'jets')

    D_name = "Lum/" + "I " + str(i)
    save_pic(D_name)

    cv2.imwrite('Jet_pic_lum/' + 'JI ' + str(i) + '.jpg', jets)

    i += 0.0025

    cv2.waitKey(0)
