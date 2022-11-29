
from liveStream import app
import face_recognition as fr
import socket
from waitress import serve

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

if __name__ == '__main__':
    serve(app, host=IPAddr, port=8080, url_scheme='RTMP', threads=6)
    