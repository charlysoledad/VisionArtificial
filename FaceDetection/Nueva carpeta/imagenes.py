import numpy
import cv2
from matplotlib import pyplot as plt


def main():


	img = cv2.imread("ovni2.png")

	img = cv2.imread("ovni2.png",cv2.IMREAD_GRAYSCALE)



	cv2.imshow('Imagen',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	matploit()

	return

def  matploit():

	img = cv2.imread("ovni2.png")
	plt.imshow(img)
	plt.xticks([]), plt.yticks([])
	plt.show()

	return


if __name__ == '__main__':
    main()