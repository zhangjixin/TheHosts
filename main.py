__author__ = 'zhang'
import os
import sys
import re
import socket
import subprocess
import ipSet

def main():
    out, err = subprocess.Popen("nslookup -q=TXT _netblocks.google.com 8.8.8.8", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    result = out.split()
    ip_list = [re.split("[':]", str(ip))[2] for ip in result if str(ip).startswith("b'ip4:")]
    print(ip_list)
    ipSet.Getipset(ip_list)

if __name__ ==  '__main__':
    main()
