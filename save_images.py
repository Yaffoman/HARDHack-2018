import cv2
import numpy as numpy
import sys
import os

if len(sys.argv) < 2:
    print('Start with file name u want to save as.')
    exit()

camera = cv2.VideoCapture(1)   # 0 on Dragon and 1 on laptop

while camera.isOpened():
    retval, im = camera.read() # 720 x 1280 camera rgb sensor
    # im = im[:, 200:1042, :]
    im = im[0:635, 200:1042, :]

    h,w,ch = im.shape
    # print('im size: ({}, {})'.format(h,w))

    cv2.imshow("Output", im)

    k = cv2.waitKey(20) & 0xff
    if k == 83 or k == 115:
        cv2.imwrite('.'.join([sys.argv[1], 'jpg']), im)
        break


# retval, im = camera.read() # 720 x 1280 camera rgb sensor
# im = im[:, 200:1042, :]
# cv2.imwrite(os.path.join('images', '.'.join(sys.argv[1], '.jpg')))

camera.release()
cv2.destroyAllWindows()
