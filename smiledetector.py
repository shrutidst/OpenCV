import cv2
import numpy as np
def changedVals(a = True):
    hmin = cv2.getTrackbarPos("Hue Min", "TrackBars")
    hmax = cv2.getTrackbarPos("Hue Max", "TrackBars")
    smin = cv2.getTrackbarPos("Sat Min", "TrackBars")
    smax = cv2.getTrackbarPos("Sat Max", "TrackBars")
    vmin = cv2.getTrackbarPos("Val Min", "TrackBars")
    vmax = cv2.getTrackbarPos("Val Max", "TrackBars")
    return hmin, hmax, smin, smax, vmin, vmax


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 65, 179, changedVals)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, changedVals)
cv2.createTrackbar("Sat Min", "TrackBars", 5, 255, changedVals)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, changedVals)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, changedVals)
cv2.createTrackbar("Val Max", "TrackBars", 240, 255, changedVals)

while True:
    plumImg = cv2.imread("images/plum.bmp")
    plumImgCanny = cv2.Canny(plumImg, 120, 150)

    plumImgHSV = cv2.cvtColor(plumImg, cv2.COLOR_BGR2HSV)

    h_min, h_max, s_min, s_max, v_min, v_max = changedVals()
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(plumImgHSV, lower, upper)
    plumPink = cv2.bitwise_and(plumImg, plumImg, mask=mask)
    cv2.imshow("img", plumImg)
    cv2.imshow("edges", plumImgCanny)
    # cv2.imshow("HSV", plumImgHSV)
    # cv2.imshow("mask", mask)
    cv2.imshow("plumPink", plumPink)
    cv2.waitKey(1)

    # save images
    cv2.imwrite("images/ImgEdges.png", plumImgCanny)
    cv2.imwrite("images/PinkExtracted.png", plumPink)
