import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
alive = True
while alive:
    # Capture
    status, imgcv = cap.read()
    # Display
    cv2.imshow("image", imgcv)
    # Pause and keyboard check
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        alive = False

# Clean up
cap.release()
cv2.destroyAllWindows()

