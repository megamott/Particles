import cv2
import numpy as np
import pylab
from mpl_toolkits.mplot3d import Axes3D


def showme(pic, name):
    cv2.imshow(name, pic)
    cv2.waitKey()
    cv2.destroyAllWindows()


jets = cv2.imread("MicroJet.jpg")
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

# showme(jets, 'lab')

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
