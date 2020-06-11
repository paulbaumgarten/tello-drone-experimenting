import numpy as np
import cv2

# Derived from https://www.pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
alive = True

red_hsv_range = (np.array([0,50,220]), np.array([10,255,255]))
green_hsv_range = (np.array([50,50,220]), np.array([90,255,255]))

while alive:
    # Capture
    status, imgcv = cap.read()
    if status:

        hsv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2HSV)
        red = cv2.inRange(hsv, red_hsv_range[0], red_hsv_range[1])
        green = cv2.inRange(hsv, green_hsv_range[0], green_hsv_range[1])

        #red_mask = cv2.cvtColor(red_mask, cv2.COLOR_HSV2BGR)
        # gray = cv2.cvtColor(red_mask, cv2.COLOR_BGR2GRAY)
        #blurred = cv2.GaussianBlur(red_mask, (11, 11), 0)
        #thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1] # any pixel value p >= 200 and sets it to 255 (white). Pixel values < 200 are set to 0 (black).
        #thresh = cv2.erode(thresh, None, iterations=2) # Clean noise by running erosions
        #thresh = cv2.dilate(thresh, None, iterations=4) # Clean noise by running dilations

        # Display
        cv2.imshow("red", red)
        cv2.imshow("green", green)
    # Pause and keyboard check
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        alive = False

# Clean up
cap.release()
cv2.destroyAllWindows()

