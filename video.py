# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 07:19:44 2020

@author: Sankhasubhra Mandal
"""
import numpy as np
import cv2
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('pedestrian.mp4')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

