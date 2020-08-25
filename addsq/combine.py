#!/usr/bin/env python
#cosine code
 
import socket
import math
from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)


HOST = "localhost"
PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall("60\n".encode("ASCII"))
rec = list(sock.recv(1024))
rec=rec[:-1]
for i,a in enumerate(rec):
    rec[i]=chr(a)
rec=float("".join(rec))
sock.close()


ang=math.pi/3
sinval=math.sin(ang)
cosval=rec
val=pow(sinval,2)+pow(cosval,2)

class Tot(Resource):
	def get(self):
		return "cos2 (60) + sin2 (60) = "+val

api.add_resource(Tot,'/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
