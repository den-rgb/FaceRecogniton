import cv2 as cv
import numpy as np
import face_recognition as fr

    
img_Obama = fr.load_image_file('BasicImages/obama.jpg')
img_Obama = cv.cvtColor(img_Obama,cv.COLOR_BGR2RGB)
img_Test = fr.load_image_file('BasicImages/obama1.jpg')
img_Test = cv.cvtColor(img_Test,cv.COLOR_BGR2RGB)
    
faceLocator = fr.face_locations(img_Obama)[0]
encodeObama = fr.face_encodings(img_Obama)[0]
cv.rectangle(img_Obama,(faceLocator[3],faceLocator[0]),(faceLocator[1],faceLocator[2]),(255,0,255),2)
    
faceLocator = fr.face_locations(img_Test)[0]
encodeTest = fr.face_encodings(img_Test)[0]
cv.rectangle(img_Test,(faceLocator[3],faceLocator[0]),(faceLocator[1],faceLocator[2]),(255,0,255),2)
    
result = fr.compare_faces([encodeObama],encodeTest)
faceDis = fr.face_distance([encodeObama],encodeTest)
print(result,faceDis)

cv.putText(img_Test,f'{result} {round(faceDis[0],2)}',(50,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    
cv.imshow('Obama',img_Obama)
cv.imshow('Test',img_Test)
cv.waitKey(0)