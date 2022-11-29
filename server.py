import eventlet
from liveStream import app
import socketio
import face_recognition as fr
import socket
from waitress import serve

sio = socketio.Server()


hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    

@sio.event
def my_message(sid, data):
    print('message ', data)
    

@sio.event
def disconnect(sid):
     print('disconnect ', sid)
    

if __name__ == '__main__':
    serve(app, host=IPAddr, port=8080, url_scheme='RTMP', threads=6)
    print(IPAddr)