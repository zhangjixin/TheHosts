import sys
import socket
import time
import connip

def selectIp(leftIp, rightIp, i):
	fw = open("../output/result" + str(i), "w")
	ip2score = {}
	cnt = 0
	for ip1 in range(leftIp[0], rightIp[0] + 1):
		for ip2 in range(leftIp[1], rightIp[1] + 1):
			for ip3 in range(leftIp[2], rightIp[2] + 1):
				for ip4 in range(leftIp[3], rightIp[3] + 1):
					ipstr = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
					#print(ipstr)
					ret, score = connIp.ConnIp(ipstr)
					if ret :
						fw.write('{0} | {1}\n'.format(ipstr, score))						
						print("bingo")
						#ip2score[ipstr] = score
						cnt += 1;
						if cnt >= 10:
							cnt = 0
							break
						#
				fw.flush()
	
	fw.close()
