from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time

# get the webcam:  
cam0 = cv2.VideoCapture(0)
#cam1 = cv2.VideoCapture(2)

# WIDTH, HEIGHT = 160,  120
WIDTH, HEIGHT = 320,  240
# WIDTH, HEIGHT = 352,  288
#WIDTH, HEIGHT = 640,  480
# WIDTH, HEIGHT = 1024,  768
# WIDTH, HEIGHT = 1280,  1024

cam0.set(3,WIDTH)
cam0.set(4,HEIGHT)

#cam1.set(3,WIDTH)
#cam1.set(4,HEIGHT)

time.sleep(2)

def decode(im) : 
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')     
    return decodedObjects


font = cv2.FONT_HERSHEY_SIMPLEX

print(cam0.get)

while(cam0.isOpened()): #or cam1.isOpened()):
    # Capture frame-by-frame
    ret, frame = cam0.read()
    #ret_1, frame_1 = cam1.read()
    # Our operations on the frame come here
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #im2 = cv2.cvtColor(frame_1, cv2.COLOR_BGR2GRAY)
         
    decodedObjects = decode(im)
    #decodedObjects2 = decode(im2)

    for decodedObject in decodedObjects: 
        points = decodedObject.polygon
     
        # If the points do not form a quad, find convex hull
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points;
         
        # Number of points in the convex hull
        n = len(hull)     
        # Draw the convext hull
        for j in range(0,n):
          cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)

        x = decodedObject.rect.left
        y = decodedObject.rect.top

        barCode = str(decodedObject.data)
        cv2.putText(frame, barCode, (0, HEIGHT-20), font, 0.6, (255,0,255), 1, cv2.LINE_AA)
               
    # Display the resulting frame
    cv2.imshow('frame',frame)
    #cv2.imshow('frame mask',im2)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'): # wait for 's' key to save 
        cv2.imwrite('Capture.png', frame)     

# When everything done, release the capture
cam0.release()
#cam1.release()
cv2.destroyAllWindows()