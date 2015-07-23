import sys

def main():
	fr = open("../output/filterIP","r")
	fw = open("../data/ip.filter","w")
	ipstr = fr.read()
	ipresult = ipstr.split("\\n")
	for ip in ipresult:
		if len(ip) < 4:
			continue
		fw.write("{0}\n".format(ip))
	fr.close()
	fw.close()
if (__name__ == '__main__'):
	main()