import sys
import iprange
import subIpSet
import time
from threading import Thread
import multiprocessing as MP

ipset = []
def doit(ipstr, que) :
	global ipset
	leftIp, rightIp = iprange.getIpRange(ipstr)
	que.put( subIpSet.Getsubipset(leftIp, rightIp))
def Getipset(ip_list) :
	global ipset
	ProcessSet = []
	que = MP.Queue()
	startT = time.time()
	for i in range(len(ip_list)) :
		ip = ip_list[i]
		p = MP.Process(target = doit, args = (ip,que))
		ProcessSet.append(p)
	for p in ProcessSet:
		p.start()
	for p in ProcessSet:
		ipset += que.get()
	for p in ProcessSet:
		p.join()
	
	print("time: {0}".format(time.time() - startT))
	print("length of ipset : {0}".format(len(ipset)))
	ProcessSet = []


if __name__ == '__main__' :
	ip_list = [ "64.18.0.0/20", "64.233.160.0/19", "216.239.32.0/19"]
	ipSet(ip_list)