#!/usr/bin/env python3


import socket
import netifaces as ni

# Automatic Identification of local IP address 
def get_local_IP(Interface):
	ni.ifaddresses(Interface)
	ip = ni.ifaddresses(Interface)[ni.AF_INET][0]['addr']	
	return ip

# Configurations
Interface 	= "eth0" 			# The name of the listening interface
UDP_IP 		= get_local_IP(Interface)	# The IP address of the listening interface
UDP_PORT 	= 5556				# The Port number used for listening
MessageCodes 	= []				# Optional
MessageCount	= 0				# 	
MessageLimit 	= 1000				# Limit for receiving messeges (-1 for continous reciption)

print("Testing UDP Sender\n")


"""
Establishing Connection listner
"""

try:
	sock = socket.socket(socket.AF_INET, # Internet
		             socket.SOCK_DGRAM) # UDP
	sock.bind((UDP_IP, UDP_PORT))
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
		data = str(data)	
		MessageCount = MessageCount + 1
		SourcePort = addr[1]
		SourceIP = addr[0]
		print("["+UDP_IP+":"+str(UDP_PORT)+"] From ["+str(SourceIP)+":"+str(SourcePort))
		print("[Message#"+str(MessageCount)+"]:"+str(data))
		print("------------------")
	else:
		print("Nothing is recived")
print("\n========================================================\n")
print("Received "+ str(MessageCount) +" messages\n")



