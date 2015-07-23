import sys

def GetSubIpSet(leftIp, rightIp):
    ipSet = set()
    for ip1 in range(leftIp[0], rightIp[0] + 1):
        for ip2 in range(leftIp[1], rightIp[1] + 1):
            for ip3 in range(leftIp[2], rightIp[2] + 1):
                for ip4 in range(leftIp[3], rightIp[3] + 1):
                    ipStr = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
                    ipSet.add(ipStr)
    return ipSet
