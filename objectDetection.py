import cv2
import numpy as np

cap = cv2.VideoCapture(0) # set camera
cap.set(3, 1280) # set frame width
cap.set(4, 720) # set frame height
cv2.namedWindow('Tracker',cv2.WINDOW_NORMAL)
cv2.namedWindow('Thresh',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Tracker',1440,720)
cv2.resizeWindow('Thresh',1440,720)
while True:
    img = cap.read()[1]
    CARD_MIN = np.array([64,90,45],np.uint8)
    CARD_MAX = np.array([145,255,181],np.uint8)

    imhsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    thresholded_image = cv2.inRange(imhsv, CARD_MIN, CARD_MAX)
    thresholded_image = cv2.medianBlur(thresholded_image, 15)

    im2, contours, hierarchy = cv2.findContours(thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    for c in contours:
    	x,y,w,h = cv2.boundingRect(c)
    	img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Tracker",img)
    cv2.imshow("Thresh",thresholded_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break