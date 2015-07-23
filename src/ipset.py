import sys
import multiprocessing as MP

import iprange
import subipset

myIpSet = set()

def doit(ipStr, que) :
	global myIpSet
	leftIp, rightIp = iprange.GetIpRange(ipStr)
	que.put(subipset.GetSubIpSet(leftIp, rightIp))

def GetIpSet(ipList) :
	global myIpSet
	processSet = []
	que = MP.Queue()
	for ip in ipList :		
		p = MP.Process(target = doit, args = (ip,que))
		processSet.append(p)
	for p in processSet:
		p.start()
	for p in processSet:
		myIpSet |= que.get()
	for p in processSet:
		p.join()
	fr = open("../data/ip.filter", "r")
	ipLines = fr.readlines()
	fr.close()
	ipFilterSet = set()
	for ip in ipLines:
		ipFilterSet.add(ip.strip())	
	myIpSet = myIpSet - ipFilterSet
	return myIpSet
	'''
	print("time: {0}".format(time.time() - startT))
	print("length of myIpSet : {0}".format(len(myIpSet)))
	
	processSet = []
	'''

if __name__ == '__main__' :
	ipList = [ "64.18.0.0/20", "64.233.160.0/19", "216.239.32.0/19"]
	GetIpSet(ipList)