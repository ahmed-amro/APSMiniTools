#!/usr/bin/env python3

import time
import socket
import sys
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


print("Testing UDP Receiver\n")

def check(Ip):
	valid = -1
	# pass the regular expression
	# and the string in search() method
	if(re.search(regex, Ip)):
		print("Valid Ip address")
		valid = 1
	else:
		print("Invalid Ip address")
		valid = 0
	return valid

if check(sys.argv[1]):
	UDP_IP = sys.argv[1]
else:
	print("The provided desticnation IP address is not valid")
	exit()

#UDP_IP = ip
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




