__author__ = 'zhang'
import os
import sys
import time
import ipset
import ipselect
import merger
import combinedhost

def main(ipList):
	startT = time.time()
	myIpSet = ipset.GetIpSet(ipList)	
	num = ipselect.selectIp(list(myIpSet))
	merger.MergerResult(num)
	combinedhost.GetHosts()
	print(time.time() - startT)  

if __name__ ==  '__main__':	
    if len(sys.argv) < 2 :
    	print("Usage : python main.py ip1/len ip2/len ...\n")
    	print("example: python main.py 64.18.0.0/20 64.233.160.0/19")
    	sys.exit()
    main(sys.argv[1:])







    '''
    out, err = subprocess.Popen("nslookup -q=TXT _netblocks.google.com", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    result = out.split()
    ip_list = [re.split("[':]", str(ip))[2] for ip in result if str(ip).startswith("b'ip4:")]
    '''
