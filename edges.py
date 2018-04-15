from filter import *

def laplace(coord):
    return sum(coord[1:5]) - 4 * coord[0]

img = open(sys.argv)
img.show()
edges = filter(img, laplace)
edges.show()img.save(%s-%s.png % (sys.argv[1][:-4], sys.argv[0][:-3]))
