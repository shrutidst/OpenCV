import cv2
import numpy as np
img = cv2.imread("resources/lavi.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (21,21), 0)

imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
# cv2.imshow("window", img)
# cv2.imshow("window2", imgGray)
# cv2.imshow("window3", imgBlur)
cv2.imshow("window", imgCanny)
cv2.imshow("window1", imgDialation)
cv2.imshow("wee", imgEroded)

cv2.waitKey(0)
# 0 means infinite delay. else its that many milliseconds.
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
#
# # we could also pass the file address which could display image
# # 0 means we are just opening the default webcam
#
# while True:
#     success, img2 = cap.read()
#     cv2.imshow("Video", img2)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindows()