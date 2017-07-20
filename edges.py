from filter import *

def laplace(coord):
    return sum(coord[1:5]) - 4 * coord[0]

img = open(sys.argv)
img.show()
edges = filter(img, laplace)
edges.show()