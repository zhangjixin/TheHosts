import sys
import time
import subprocess
import os
import socket
import telnetlib
import time
from threading import Thread
import multiprocessing as MP
'''
host = '195.122.16.40'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)
start = time.time()
ret = sock.connect_ex((host, 443))

if ret :
	print("connect success")
else :
	print(time.time() - start)
	print("failed")
sock.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)
ret = sock.connect_ex((host, 80))
if ret:
	print("hhhh")
else :
	print("www")

sock.close()
#delay = subprocess.Popen(["ping","-c","3",'www.google.com'], stdout=subprocess.PIPE).communicate()[0]

#print(type(delay), delay)
'''
def myfun(i) :
	print("sleeping 5 sec from thread " + str(i))
	time.sleep(3);
	print("finish sleelping from thread " + str(i))
def threadtest():
	threads = []
	startT = time.time()
	for i in range(1, 5):
		t = Thread(target = myfun, args = (i,))
		threads.append(t)
	for i in range(len(threads)):
		threads[i].start()
	for i in range(len(threads)):
		threads[i].join()
	print("time: {0}".format(time.time() - startT))
	print("hhhhhhh")
def multiProcessTest():
	ProcessSet = []
	startT = time.time()
	for i in range(1, 5):
		p = MP.Process(target = myfun, args = (i,))
		ProcessSet.append(p)
	for p in ProcessSet:
		p.start()
	for p in ProcessSet:
		p.join()
	print("time: {0}".format(time.time() - startT))
	print("multiprocessing")
def Poolcallback(result):
	print("done one {0}".format(result))
def PoolTest():
	ProcessSet = []
	pool = MP.Pool(processes = 4)
	startT = time.time()
	for i in range(1, 5):
		pool.apply(myfun, args = (i,))
		#ProcessSet.append(p)
	
	#for p in ProcessSet:
	pool.close()
	pool.join()
	print("time: {0}".format(time.time() - startT))
	print("multiprocessing")
if (__name__ == '__main__'):
	#multiProcessTest()
	#threadtest()
	PoolTest()
