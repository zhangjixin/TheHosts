import sys
import re

def GetIpRange(ipstr) :
	ip = re.split("[./]", ipstr)
	leftRange = [0,0,0,0]
	rightRange = [0,0,0,0]
	fixedLen = int(ip[4])

	for i in range(0,4) :
		if fixedLen == 0 :
			rightRange[i] = 255
			continue
		ipInNum = int(ip[i])			
		if fixedLen >= 8 :
			leftRange[i] = ipInNum
			rightRange[i] = ipInNum
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
			leftRange[i] = leftIp
			rightRange[i] = rightIp

	return leftRange, rightRange
	


if __name__ == '__main__' :
	iprange()