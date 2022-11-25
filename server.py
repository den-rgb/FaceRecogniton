import eventlet
from AttendanceProject import app
import socketio
import face_recognition as fr

sio = socketio.Server()
appServer = socketio.WSGIApp(sio, app)

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
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), appServer)