from filter import *

def avg(num):
	sum = 0
	count = 0

	for i in num:
		sum = sum + i
		count = count + 1
	return sum/count


img = open(sys.argv)
img.show()
img = filter(img, avg)
img.show()
img.save(%s-%s.png % (sys.argv[1][:-4], sys.argv[0][:-3]))
