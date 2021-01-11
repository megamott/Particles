import cv2
import numpy as np


# ----- Show me image -----
def showme(pic, name):
    cv2.imshow(name, pic)
    cv2.waitKey()
    cv2.destroyAllWindows()


# ----- Draw green circles for all and blue circle for one from roi -----
def draw_circles(final_image, roi_of_final_image):
    gray_image = cv2.cvtColor(final_image, cv2.COLOR_BGR2GRAY)
    blur_image = cv2.medianBlur(gray_image, 5)
    # cimg = cv2.cvtColor(blur_image, cv2.COLOR_GRAY2BGR)

    gray_roi = cv2.cvtColor(roi_of_final_image, cv2.COLOR_BGR2GRAY)
    blur_roi = cv2.medianBlur(gray_roi, 5)
    # cimg_roi = cv2.cvtColor(blur_roi, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(blur_image, cv2.HOUGH_GRADIENT, 1, param1=40, param2=20,
                               minRadius=10, maxRadius=25, minDist=20)

    roi_circles = cv2.HoughCircles(blur_roi, cv2.HOUGH_GRADIENT, 1, param1=40, param2=20,
                                   minRadius=10, maxRadius=25, minDist=20)

    circles = np.uint16(np.around(circles))
    roi_circles = np.uint16(np.around(roi_circles))

    for i in circles[0, :]:
        cv2.circle(final_image, (i[0], i[1]), i[2], (0, 255, 0), 3)

    for i in roi_circles[0, :]:
        cv2.circle(roi_of_final_image, (i[0], i[1]), i[2], (255, 0, 0), 3)

    showme(final_image, 'particles')
    # showme(roi_of_final_image, 'roi')
    # cv2.imwrite('Jet_pic_lum/Particles.jpg', final_image)


# ----- Finder of true combination of coefficients in Haw Transform -----
def find_necessary_combination_to_how_transform(image_name):
    for j in range(10, 100):
        for k in range(30):
            final_pic = cv2.imread(image_name)
            gray_pic = cv2.cvtColor(final_pic, cv2.COLOR_BGR2GRAY)
            blur_pic = cv2.medianBlur(gray_pic, 5)
            try:
                circles = cv2.HoughCircles(blur_pic, cv2.HOUGH_GRADIENT, 1, param1=j, param2=k,
                                           minRadius=10, maxRadius=25, minDist=20)
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    cv2.circle(final_pic, (i[0], i[1]), i[2], (0, 255, 0), 3)

                showme(final_pic, str(j) + " " + str(k))

            except Exception:
                print(j)


name = "7.17_IZ/Z 0.017.jpg"
jets = cv2.imread(name)

# For Macbook
jets = cv2.resize(jets, (800, 600))

# True Roi for jets from "2.5_IZ" folder
# roi = jets[280:360, 760:840]
# roi = jets[170:220, 700:750]

roi = jets[250:350, 350:450]

showme(jets, 'particles')
showme(roi, 'roi')

draw_circles(jets, roi)
find_necessary_combination_to_how_transform(name)

