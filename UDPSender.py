#!/usr/bin/env python3

import time
import socket
import netifaces as ni


print("Testing UDP Receiver\n")

ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

UDP_IP = ip
UDP_PORT = 10111
MESSAGE = b"Hello, World!"

#print("UDP target IP: %s" % UDP_IP)
#print("UDP target port: %s" % UDP_PORT)
#print("message: %s" % MESSAGE)


try:
	while True:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
		print("Message ("+ str(MESSAGE)+ ") Sent to ["+str(UDP_IP)+":"+str(UDP_PORT)+"], waiting for 3 seconds")
		time.sleep(3)
except KeyboardInterrupt:
    	pass




