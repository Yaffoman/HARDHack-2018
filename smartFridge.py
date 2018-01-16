#!/usr/bin/env python
from GPIOLibrary import GPIOProcessor
import time
import mraa

GP = GPIOProcessor()
import cv2, sys

light_pin = mraa.Gpio(24)
light_pin.dir(mraa.DIR_OUT)


def get_image():
    IMAGE_FILE = "output.jpg"
    # Init webcam
    vc = cv2.VideoCapture(1)

    # Check if the webcam init was successful
    if vc.isOpened():  # try to get the first frame
        retval, frame = vc.read()
    else:
        sys.exit(1)

    # If webcam read successful, loop indefinitely
    if retval:
        # Write some text onto the frame
        # Show the image on the screen
        # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
        cv2.imshow("Inside Fridge", frame)
        cv2.imwrite(IMAGE_FILE, frame)

        # Grab next frame from webcam
        retval, frame = vc.read()

    return True

try:
    while True:
        value = light_pin.read()
        print value
        if value:
            print "The light is on"
            get_image()
        else:
            print "The light is off"
        time.sleep(1)
finally:
    GP.cleanup()
