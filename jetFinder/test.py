import cv2
import numpy as np


def showme(pic, name):
    cv2.imshow(name, pic)
    cv2.waitKey()
    cv2.destroyAllWindows()


name = "I от Z/Z 0.04.jpg"
jets = cv2.imread(name)
gray = cv2.cvtColor(jets, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

roi = jets[280:360, 760:840]
gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
img_roi = cv2.medianBlur(gray_roi, 5)
cimg_roi = cv2.cvtColor(img_roi, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, param1=40, param2=20,
                           minRadius=10, maxRadius=25, minDist=20)

roi_circles = cv2.HoughCircles(img_roi, cv2.HOUGH_GRADIENT, 1, param1=40, param2=20,
                               minRadius=10, maxRadius=25, minDist=20)

circles = np.uint16(np.around(circles))
roi_circles = np.uint16(np.around(roi_circles))

for i in circles[0, :]:
    cv2.circle(jets, (i[0], i[1]), i[2], (0, 255, 0), 3)

for i in roi_circles[0, :]:
    cv2.circle(roi, (i[0], i[1]), i[2], (255, 0, 0), 3)


showme(jets, 'particles')
# showme(roi, 'roi')
# cv2.imwrite('Jet_pic_lum/Particles.jpg', jets)


# for j in range(40, 100):
#     for k in range(30):
#         jets = cv2.imread(name)
#         try:
#             circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, param1=j, param2=k,
#                                        minRadius=10, maxRadius=25, minDist=20)
#             circles = np.uint16(np.around(circles))
#             for i in circles[0, :]:
#                 cv2.circle(jets, (i[0], i[1]), i[2], (0, 255, 0), 3)
#
#             showme(jets, str(j) + " " + str(k))
#
#         except(Exception):
#             print(j)
