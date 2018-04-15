from filter import *

def laplace(coord):
    return sum(coord[1:5]) - 4 * coord[0]

def minus(A, B):
    width, height = A.size

    imgdup = A.copy()

    pixels = imgdup.load()

    A = A.copy().load()
    B = B.copy().load()

    for x in range(width):
        for y in range(height):
            pixels[x, y] = A[x, y] - B[x,y]
    return imgdup

img = open(sys.argv)
img.show()

edges = filter(img, laplace)

minus(img, edges).show()



img.save(%s-%s.png % (sys.argv[1][:-4], sys.argv[0][:-3]))
