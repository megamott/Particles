import cv2
import numpy as np


def showme(pic, name):
    cv2.imshow(name, pic)
    cv2.waitKey()
    cv2.destroyAllWindows()


jets = cv2.imread("MicroJet.jpg")
# lab = cv2.cvtColor(jets, cv2.COLOR_BGR2LAB)

for x in range(jets.shape[1]):
    for y in range(jets.shape[0]):
        b, g, r = jets[y, x]
        lum = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
        print("coordinates of: " + str(x) + " " + str(y) + " are: " + str(r) + " " + str(g) + " " + str(b)
              + " and luminance: " + str(lum))

showme(jets, 'lab')