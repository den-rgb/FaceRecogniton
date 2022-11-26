import cv2 as cv
import numpy as np
import face_recognition as fr
import os
from datetime import datetime
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from sklearn.metrics import accuracy_score
import socket

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
app = Flask(__name__)
socketioApp = SocketIO(app)

path = 'ClassPictures'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for c1 in myList:
    curImg = cv.imread(f'{path}/{c1}')
    images.append(curImg)
    classNames.append(os.path.splitext(c1)[0].upper())
print(classNames)

def findEnc(images):
    encodeList = []
    for img in images:
        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


def gen_frames():
    encodeListKnown = findEnc(images)
    print('Encode Complete')

    capture = cv.VideoCapture(0)

    while True:
        success, img = capture.read()
        imgs = cv.resize(img,(0,0),None,0.25,0.25)
        imgs = cv.cvtColor(imgs,cv.COLOR_BGR2RGB)

        faceCurrFrame = fr.face_locations(imgs)
        encodeCurrFrame = fr.face_encodings(imgs,faceCurrFrame)

        for encodeFace, faceLoc in zip(encodeCurrFrame,faceCurrFrame):
            matches = fr.compare_faces(encodeListKnown, encodeFace)
            faceDist = fr.face_distance(encodeListKnown,encodeFace)
            print(faceDist)
            matchIndex = np.argmin(faceDist)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                percentage = np.round((faceDist[matchIndex]-100)*(-1),2) #percentage match
                print(name)
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv.rectangle(img,(x1,y1),(x2,y2),(200,30,90),2)
                cv.rectangle(img,(x1,y2-35),(x2,y2),(200,30,90),cv.FILLED)
                cv.putText(img,name,(x1+6,y2-6),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                cv.putText(img,str(percentage)+"%",(x1+120,y2-10),cv.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                markAttendance(name)

        ret, buffer = cv.imencode('.jpg', img)
        img = buffer.tobytes()

        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')
        
        if cv.waitKey(1) == ord('q'): 
            break 

    cv.destroyAllWindows() #close all windows

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    #Video streaming Home Page
    return render_template('index.html')

def run():
    socketioApp.run(app)

if __name__ == '__main__':
    socketioApp.run(app)



