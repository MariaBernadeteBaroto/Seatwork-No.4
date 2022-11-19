#Creating Security cam using python

#Install Python package opencv
import cv2

#Initialize computer camera
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Computer Cam', frame1)



#Identifyiing movements
#Initializing warning sound