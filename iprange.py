import sys
import socket
import re


def getIpRange(ipstr) :
	ip = re.split("[./]", ipstr)

	LeftRange = [0,0,0,0]
	RightRange = [0,0,0,0]
	fixedLen = int(ip[4])

	for i in range(0,4) :
		if fixedLen == 0 :
			RightRange[i] = 255
			continue
		ipInNum = int(ip[i])			
		if fixedLen >= 8 :
			LeftRange[i] = ipInNum
			RightRange[i] = ipInNum
			fixedLen -= 8
		else :
			leftIp = 0
			rightIp = 0
			for j in range(7,-1,-1):
				num = 1 << j
				if (fixedLen <= 0):
					rightIp += num
				elif ipInNum & num:
					leftIp += num
					rightIp += num
				fixedLen -= 1				
			LeftRange[i] = leftIp
			RightRange[i] = rightIp

	return LeftRange, RightRange
	


if __name__ == '__main__' :
	iprange()