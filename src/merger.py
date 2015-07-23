import sys

def MergerResult(num):
	resultMap = {}
	for i in range(num):
		fr = open("../output/result" + str(i), "r")
		lines = fr.readlines()
		fr.close()
		for line in lines:
			ps = line.split(" | ")
			if len(ps) == 2:
				resultMap[ps[0].strip()] = float(ps[1].strip())

	sortedIP = sorted(resultMap, key = resultMap.get)
	fw = open("../output/ip.result", "w")
	for ip in sortedIP:
		fw.write("{0}\n".format(ip))
	fw.close()

if (__name__ == '__main__'):
	MergerResult(4)