import cv2
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier('opencv-master/data/haarcascades/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('opencv-master/data/haarcascades/haarcascade_eye.xml')
hand_cascade = cv2.CascadeClassifier('opencv-master/data/haarcascades/haarcascade_hand.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)
n_img = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        n_img+=1
        img_item = str(n_img)+".png"
        #cv2.imwrite(img_item, img)

        #Recognize? deep learned model predict keras tensorflow pytorch scikit lear
        id_, conf = recognizer.predict(roi_gray)
        if conf>=45: #and conf <=85:
            #cv2.rectangle(img,(x,y), (x+w-15,y-35),(22,255,227),cv2.FILLED)
            cv2.putText(img, labels[id_].title(), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255),2, cv2.LINE_AA)
            #print(id_)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(img, "Desconocido", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255),2, cv2.LINE_AA)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            
        hands = hand_cascade.detectMultiScale(gray)
        for (hx, hy, hw, hh) in hands:
            cv2.rectangle(roi_color, (hx, hy), (hx+hw, hy+hh), (0, 255, 0), 2)
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Deteccion de Caras OpenCV',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()