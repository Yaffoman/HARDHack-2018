# This script is for continuous video capture
# In addition it uses opencv to transform
# the video frams to HSV and displays the video stream 
import cv2,sys
import time
import numpy as np

def nothing(x):
    pass

# init webcam
vc = cv2.VideoCapture(0)

# allow the camera to warmup
time.sleep(0.1)

# Create a window for later use
cv2.namedWindow('result')
h, s, v = 100, 100, 100
img_low = np.zeros((15,512,3),np.uint8)

# Create a track bar
cv2.createTrackbar('h','result', 0, 255, nothing)
cv2.createTrackbar('s','result', 0, 255, nothing)
cv2.createTrackbar('v','result', 0, 255, nothing)

if vc.isOpened():
    retval,frame = vc.read()
else:
    sys.exit(1)

# capture frames from the camera
while True:
    retval, frame = vc.read()

    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('result', img_low)
    # Get info from trackbar and appy to the result
    h =  cv2.getTrackbarPos('h','result')
    s =  cv2.getTrackbarPos('s','result')
    v =  cv2.getTrackbarPos('v','result')
    img_low[:] = [h,s,v]
    # define the range of the blue color in hsv
    lower_green = np.array([h,s,v])
    upper_green = np.array([255, 255, 255])

    # Threshold the hsv image to get only blue colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    #Bitwise AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask = mask)

    
    # show the frame
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Res", res)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
