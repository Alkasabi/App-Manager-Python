import os
import socket
import serial
import time
import json


UDP_IP = "127.0.0.1"
UDP_PORT = 1122

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

io={
	"p1":True,
	"p2":False,
	"p3" : True
  }


while True:
	time.sleep(1)
	msg=json.dumps(io, sort_keys=True)
	packet01=msg.encode(encoding='UTF-8',errors='strict')
	sock.sendto(packet01, (UDP_IP, UDP_PORT))
	pass