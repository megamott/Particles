import numpy as np
import cv2
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
from collections import Counter

set_matplotlib_formats('svg')


def show_video(video):
    array = []

    while video.isOpened():
        ret, frame = video.read()

        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        except cv2.error:
            print("End of the video")
            break

        blur = cv2.medianBlur(gray, 5)
        cimg = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)

        roi, gray_roi = crop_video(cimg, gray)

        if ret:

            circles = find_circles(gray_roi)

            if circles is None:
                pass
                # print("no circle 1")
            else:
                circles = np.uint16(np.around(circles))
                if circles is None:
                    pass
                    # print("no circle 2")
                else:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    for i in circles[0, :]:
                        roi = cv2.putText(roi, str(i[0]) + '; ' + str(i[1]), (i[0], i[1]),
                                          font, 1, (0, 0, 0), 2,
                                          cv2.LINE_AA)
                        cv2.circle(roi, (i[0], i[1]), i[2], (0, 0, 0), 2)
                        cv2.circle(roi, (i[0], i[1]), 2, (0, 255, 255), 3)
                        cv2.imshow('cimg', cimg)
                        cv2.imshow('roi', roi)
                        print(circles[0])
                        array.append(circles[0])

            if cv2.waitKey(1) == ord('q'):
                break

    print("   ")
    draw_graph(array)

    video.release()
    cv2.destroyAllWindows()


def crop_video(video, gray_video):
    roi = video[210:300, 480:660]
    gray_roi = gray_video[210:300, 480:660]
    return roi, gray_roi


def find_circles(gray_video):
    circles = cv2.HoughCircles(gray_video, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=20,
                               minRadius=0, maxRadius=25)
    return circles


def draw_graph(array):
    x_array = []
    y_array = []

    for i in range(len(array)):
        x_array.append(array[i][0][0])
        y_array.append(array[i][0][1])

    print(x_array)
    print(y_array)

    x = dict(Counter(x_array))
    y = dict(Counter(y_array))

    print(x)
    print(y)

    # plt.bar(x.keys(), x.values())
    # plt.bar(y.keys(), y.values())
    # plt.title('Particles')

    plt.hist(x_array, 8)

    plt.xlabel('Coordinate')
    plt.ylabel('Quantity')
    plt.show()


# def create_histogram():
#     mu, sigma = 38, 0.1
#     s = np.random.normal(mu, sigma, 1000)
#
#     bins = 8
#
#     plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
#              np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=3, color='y')


particles = cv2.VideoCapture('particless.mp4')
show_video(particles)
