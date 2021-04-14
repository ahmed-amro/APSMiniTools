#!/usr/bin/env python3


import socket
#import netifaces as ni
import time
import sys
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

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

# Automatic Identification of local IP address 
#def get_local_IP(Interface):
#	ni.ifaddresses(Interface)
#	ip = ni.ifaddresses(Interface)[ni.AF_INET][0]['addr']	
#	return ip

print("First = " + str(sys.argv[1]) + "Second = "+ str(sys.argv[2]))
if check(sys.argv[1]):
	UDP_IP = sys.argv[1]
else:
	print("The provided local IP address is not valid")
	exit()

if check(sys.argv[2]):
	ReceiverUDP_IP = sys.argv[2]
else:
	print("The provided desticnation IP address is not valid")
	exit()


# Configurations
Interface 		= "eth0" 			# The name of the listening interface
#UDP_IP 			= get_local_IP(Interface)	# The IP address of the listening interface
UDP_PORT 		= 10111				# The Port number used for listening
#ReceiverUDP_IP 		= 				# The IP address of the receiver 
ReceiverUDP_PORT	= 5556				# The Port number used for sending
MessageCodes 		= []				# Optional
MessageCount		= 0				# 	
MessageLimit 		= 1000				# Limit for receiving messeges (-1 for continous reciption)

print("Testing UDP Receiver/Sender\n")


"""
Establishing Connection with NMEA sender
"""

try:
	sock = socket.socket(socket.AF_INET, # Internet
		             socket.SOCK_DGRAM) # UDP
	sock.bind((UDP_IP, UDP_PORT))
	sock2 = socket.socket(socket.AF_INET, # Internet
		             socket.SOCK_DGRAM) # UDP
	sock2.bind((ReceiverUDP_IP, ReceiverUDP_PORT))
except:
	print("Something went wrong: couldn't establish connection")
	pass


"""
Receiving and printing messages
"""


print("Waiting for the first "+str(MessageLimit)+" messages")
print("Listening on ["+str(UDP_IP)+":"+str(UDP_PORT)+"]")
while MessageCount < MessageLimit:
	"""
	Receiving Data
	"""
	try:
		data, addr = sock.recvfrom(512) # buffer size is 1024 bytes
	except:
		print("Something went wrong: couldn't receive")
		pass		
	
	if data != "":	
		data =data	
		MessageCount = MessageCount + 1
		SourcePort = addr[1]
		SourceIP = addr[0]

		print("[Message#"+str(MessageCount)+"]")
		print("[Received:"+str(UDP_IP)+":"+str(UDP_PORT)+"]")
		print("[Origin:"+str(SourceIP)+":"+str(SourcePort)+"]")
		print("--------")
		print("Content:")
		print(str(data))
		print("--------")

		try:
			#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
			sock2.sendto(data, (ReceiverUDP_IP, ReceiverUDP_PORT))
			print(" --> Forwarded to ["+str(ReceiverUDP_IP)+":"+str(ReceiverUDP_PORT)+"]")			
			print("########################################S")
		except KeyboardInterrupt:
			print("Something went wrong: couldn't send")
			pass





	else:
		print("Nothing is recived")
print("\n========================================================\n")
print("Received "+ str(MessageCount) +" messages\n")



