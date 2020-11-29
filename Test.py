import cv2
import numpy as np


def showme(pic, name):
    cv2.imshow(name, pic)
    cv2.waitKey()
    cv2.destroyAllWindows()


jets = cv2.imread("MicroJet.jpg")
gray = cv2.cvtColor(jets, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

for j in range(100):
    for k in range(30):
        jets = cv2.imread("MicroJet.jpg")
        try:
            circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, param1=j, param2=k,
                                       minRadius=0, maxRadius=10, minDist=40)
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                cv2.circle(jets, (i[0], i[1]), i[2], (0, 255, 0), 1)

            showme(jets, str(j) + " " + str(k))

        except(Exception):
            print(j)
