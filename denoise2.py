from filter import *

def median(data):

	data = sorted(data)

	index = len(data)/2

	return data[index]

img = open(sys.argv)
img.show()
img = filter(img, median)
img.show()
img.save(%s-%s.png % (sys.argv[1][:-4], sys.argv[0][:-3]))
