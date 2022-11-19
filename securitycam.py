#Creating Security cam using python

#Install Python package opencv
import cv2

#Initialize computer camera
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()     #Identifying movements
    diff = cv2.absdiff(frame1, frame2)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Computer Cam', diff)


 
#Initializing warning sound