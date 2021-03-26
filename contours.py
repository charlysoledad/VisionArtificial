import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def onKey(key):
	global exposure
	if key == ord("-") or key == ord("_"):
        exposure -= 1
        cap.set(cv2.CAP_PROP_EXPOSURE, exposure)
    if key == ord("=") or key == ord("+"):
        exposure += 1
        cap.set(cv2.CAP_PROP_EXPOSURE, exposure)

def initCapture(cap):
	global exposure
    exposure = cap.get(cv2.CAP_PROP_EXPOSURE)
    cap.set(cv2.CAP_PROP_EXPOSURE, exposure)

while(1):

	global exposure
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([0,0,255])
    upper_blue = np.array([130,255,255])


    lower_green = np.array([0,255,0])
    upper_green = np.array([130,255,130])

    lower_red = np.array([255,0,0])
    upper_red = np.array([255,255,130])

    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask_green)
    
    cv2.imshow('frame',frame)
    #cv2.imshow('BLUE M',mask_blue)
    #cv2.imshow('RED M',mask_red)
    cv2.imshow('GREEN M',mask_green)
    cv2.imshow('res',res)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key != 0xFF:
        onKey(key)

cv2.destroyAllWindows()