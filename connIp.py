import sys
import socket
import time

def connIp(host) :
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)	
	if sock.connect_ex((host, 80)):
		return False, 0
	sock.close()

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)	
	startTime = time.time()
	if sock.connect_ex((host, 443)):
		return False, 0	
	endTime = time.time()
	sock.close()
	return True, endTime - startTime	
	
