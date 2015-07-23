import sys

def MergerResult(num):	
	fr = open("../data/ip.host", "r")
	lines = fr.readlines()
	fr.close()
	hostSet = set()
	for host in lines:
		ps = host.split()
		if (len(ps) == 2):
			hostSet.add(ps[1].strip())
	
	fw = open("../data/ip.host2", "w")	
	for host in hostSet:
		fw.write("{0}\n".format(host))
	fw.close()
	

if (__name__ == '__main__'):
	MergerResult(3)