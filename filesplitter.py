import sys

if __name__ == "__main__":
	fout = []
	percent = []
	try:
		fin = open(sys.argv[1], "r")
		for i in range(2, len(sys.argv), 2):
			percent.append(int(sys.argv[i + 1]))
	except:
		print "Usage: python filesplitter.py <in name> <out1 name> <percent1> <out2 name> <percent2> ..."
		sys.exit()

	if sum(percent) > 100:
		print "Error: can't have %d\%" %(sum(percent))
		sys.exit()

	try:
		for i in range(2, len(sys.argv), 2):
			fout.append(open(sys.argv[i], "w"))
	except:
		print "Error: couldn't open files\nUsage: python filesplitter.py <in name> <out1 name> <percent1> <out2 name> <percent2> ..."
		sys.exit()

	funcs = []
	count = 0
	for i, p in enumerate(percent):
		count += p
		for j in range(0, p):
			funcs.append(fout[i].write)

	for i in range(count, 100):
		funcs.append(None)

	s = fin.readline()
	i = 0
	while len(s) > 0:
		if funcs[i] != None:
			funcs[i](s)
		i += 1
		if i >= 100:
			i = 0
		s = fin.readline()



