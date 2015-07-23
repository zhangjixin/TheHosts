import sys

def GetHosts():
	fr = open("../output/ip.result", "r")
	lines = fr.readlines()
	fr.close()
	ipSet = set()
	for ip in lines:
		ipSet.add(ip.strip())
	fr = open("../data/ip.host", "r")
	lines = fr.readlines()
	fr.close()
	hostSet = set()
	for host in lines:
		hostSet.add(host.strip())
	
	fw = open("../output/hosts", "w")
	cnt = 0
	for ip in ipSet:		
		for host in hostSet:
			fw.write("{0}   {1}\n".format(ip, host))
		cnt += 1
		if (cnt == 5):
			break
	fw.close()
	

if (__name__ == '__main__'):
	GetHosts()