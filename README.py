# BirdRepellerUsingOpenCV
# This Project ensures that it reduces farmer effort in agricultural fields
import cv2
from playsound import playsound
import winsound
bird1_cascade = cv2.CascadeClassifier('bird1.xml')
 
cap = cv2.VideoCapture('finalbird.mp4')

while 1:   
    ret, img = cap.read() 
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    birds1 = bird1_cascade.detectMultiScale(gray,1.3, 5)
    count=0
    for (x,y,w,h) in birds1:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        l = cv2.putText(img, 'Bird', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
        if(l.any()):
            count+=1
        if(count>0):
            winsound.PlaySound("SystemExit",winsound.SND_ALIAS)
 
 
    cv2.imshow('img',img)
 
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()
