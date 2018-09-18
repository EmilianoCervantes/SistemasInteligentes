#!/usr/bin/python

import _thread
import socket
import struct

# message = 'Alfred y Emiliano'
multicast_group = ('224.3.29.71', 7777)
clients = []

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


def send_message(threadName, message):
	try:
		# Send data to the multicast group
		print("sending ", message)
		sent = sock.sendto(message.encode(), multicast_group)
		
		# Look for responses from all recipients
		while True:
			print('waiting to receive')
			try:
				data, server = sock.recvfrom(16)
			except socket.timeout:
				print('timed out, no more responses')
				break
			else:
				print('received "%s" from %s' % (data, server))
				print(data)
				
			message = data.decoce("utf-8")
			if "SALUTATIONS" in message:
				uid = message.split("::")[1]
				clients.append(uid)
				
			print('sending acknowledgement to', address)
	
	finally:
		print('closing socket')
		sock.close()


# Define a function for the thread

# Create two threads as follows
try:
	_thread.start_new_thread(send_message, ("Thread-1", "Alfredo", ))
	_thread.start_new_thread(send_message, ("Thread-2", "Emiliano", ))
finally:
	print("Error: unable to start thread")

while 1:
   pass