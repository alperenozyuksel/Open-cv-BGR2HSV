import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,300)
cv2.createTrackbar("Hue Min","Trackbars",0,179,nothing)
cv2.createTrackbar("Hue Max","Trackbars",179,179,nothing)
cv2.createTrackbar("Satur Min","Trackbars",0,255,nothing)
cv2.createTrackbar("Satur Max","Trackbars",255,255,nothing)
cv2.createTrackbar("Value Min","Trackbars",0,255,nothing)
cv2.createTrackbar("Value Max","Trackbars",255,255,nothing)



while True:
    img = cv2.imread("sigara_dumani.jpg")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("Satur Min","Trackbars")
    s_max = cv2.getTrackbarPos("Satur Max","Trackbars")
    v_min = cv2.getTrackbarPos("Value Min","Trackbars")
    v_max = cv2.getTrackbarPos("Value Max","Trackbars")
    print(h_min,s_min,v_min)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    cv2.imshow("Masked",mask)
    cv2.imshow("Image",img)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

