import cv2
import numpy as np

cass=cv2.dlib.get_frontal_face_detector()
cap=cv2.VideoCapture()
while True:
    _,frame=cap.read()
    face_det=cass(frame,1.2)
    for i in face_detect:
        l,t,r,b=i.left(),i.top(),i.right(),i.bottom()
        cv2.rectangle(frame,(l,t),(r,b),(0,255,0),2)
        cv2.putText(frame,"match found",(r,b+10),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
        cv2.imshow("sabari",frame)
    if cv2.WaitKey(1)==27:
        break
cap.release()

#sdfkajsgh apsfhg uhg sugh sadiupgahs fug
lksadfj d doif wdfo 

