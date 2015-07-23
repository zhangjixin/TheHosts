import sys
import iprange
import selectIP
import time
from threading import Thread
import multiprocessing as MP

def doit(ipstr, i) :
	leftIp, rightIp = iprange.getIpRange(ipstr)
	selectIP.selectIp(leftIp, rightIp, i)

def Poolcallback(result):
	print("pool done")
def main() :
	ip_list = [ "64.18.0.0/20", "64.233.160.0/19", "216.239.32.0/19"]	
	ProcessSet = []
	startT = time.time()
	for i in range(len(ip_list)) :
		ip = ip_list[i]
		p = MP.Process(target = doit, args = (ip, i))
		ProcessSet.append(p)
	for p in ProcessSet:
		p.start()
	for p in ProcessSet:
		p.join()
	print("time: {0}".format(time.time() - startT))
	print("Done")

'''
	#ProcessSet = []
	pool = MP.Pool(processes = 4)
	startT = time.time()
	for i in range(len(ip_list)) :
		ip = ip_list[i]
		pool.apply(doit, args = (ip, i))
		#p = pool.apply_async(doit, args = (ip, i), calback = Poolcallback)
		#ProcessSet.append(p)	
	#for p in ProcessSet:
	pool.close()
	pool.join()
	
	print("time: {0}".format(time.time() - startT))
	print("Done")

def main() :
	ip_list = [ "64.18.0.0/20", "64.233.160.0/19", "216.239.32.0/19"]	
	ProcessSet = []
	pool = MP.Pool(processes = 4)
	startT = time.time()
	for i in range(len(ip_list)) :
		ip = ip_list[i]
		p = pool.apply_async(doit, args = (ip, i), calback = Poolcallback)
		ProcessSet.append(p)	
	for p in ProcessSet:
		p.close()
		p.join()

	print("time: {0}".format(time.time() - startT))
	print("Done")
'''
if __name__ == '__main__' :
	main()