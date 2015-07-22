import sys
import socket
import time
import connIp


def Getsubipset(leftIp, rightIp):
    ipset = []
    for ip1 in range(leftIp[0], rightIp[0] + 1):
        for ip2 in range(leftIp[1], rightIp[1] + 1):
            for ip3 in range(leftIp[2], rightIp[2] + 1):
                for ip4 in range(leftIp[3], rightIp[3] + 1):
                    ipstr = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
                    ipset.append(ipstr)
    return ipset
