import sys
import socket
import time
import multiprocessing as MP

import ipconn

def doit(ipSet, i, lock):
	fw = open("../output/result" + str(i), "w")
	filterSet = set()
	for ip in ipSet:
		ret, score = ipconn.IpConnect(ip)
		if ret :
			fw.write('{0} | {1}\n'.format(ip, score))
		else:
			filterSet.add(ip)
	fw.close()
	lock.acquire()
	fw = open("../data/ip.filter", "a")
	for ip in filterSet:
		fw.write(ip)
		fw.write('\n')
	fw.close()
	lock.release()
			

def selectIp(ipSet):
	ipSetLen = len(ipSet)
	processNum = 4
	ipPoll = [ipSet[ipSetLen//processNum*(i-1) : ipSetLen//processNum * i] for i in range(1, processNum)]
	ipPoll.append(ipSet[ipSetLen//processNum * (processNum-1) : ])
	lock = MP.Lock()
	processSet = []
	que = MP.Queue()
	for i in range(processNum) :
		ip = ipPoll[i]	
		p = MP.Process(target = doit, args = (ip, i, lock))
		processSet.append(p)
	for p in processSet:
		p.start()
	for p in processSet:
		p.join()
	return processNum
	
	