#!/usr/bin/env python
import cv2, sys

IMAGE_FILE = "output.jpg"
# Init webcam
vc = cv2.VideoCapture(1)

# Check if the webcam init was successful
if vc.isOpened(): # try to get the first frame
    retval, frame = vc.read()
else:
    sys.exit(1)

# If webcam read successful, loop indefinitely
while retval:
    frame = frame[0:635, 200:1042, :]

    # Write some text onto the frame
    # Show the image on the screen
    # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
    cv2.imshow("DB410c Workshop #3: Show Video", frame)
    print('size {}'.format(frame.shape[:2]))
    # cv2.imwrite(IMAGE_FILE, frame)

    # Grab next frame from webcam
    retval, frame = vc.read()

    # Exit program after waiting for a pressed key
    # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#waitkey
    if cv2.waitKey(1) == 27:
        break