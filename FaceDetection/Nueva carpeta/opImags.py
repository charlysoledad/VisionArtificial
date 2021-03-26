import numpy as np
import cv2

def main():
	
	#Cargar imagen
	img = cv2.imread("fondo.jpg")

	px = img[555,888]

	img[100,100] = [255,255,255]
	
	unirImagenes()

	return


def capas():
	#Division de capas de imagen
	img = cv2.imread("kakashiA.jpg")

	b,g,r = cv2.split(img)
	img = cv2.merge((b,g,r))

	cv2.imshow("dst", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return

def blending():

	#Cargar Imagen
	img1 = cv2.imread("fon.jpg")
	img2 = cv2.imread("fon2.jpg")

	#mezclar
	dst = cv2.addWeighted(img2,0.7,img1,0.3,0)

	cv2.imshow("dst", dst)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return


def region():
	img = cv2.imread("fon.jpg")

	region = img[280:360, 210:270]

	img[0:30, 100:160] = region

	cv2.imshow("Maquina", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return	


def unirImagenes():
	#Cargar imagenes
	img1 = cv2.imread("fon.jpg")
	img2 = cv2.imread("penoles.png")

	filas,cols,canales = img2.shape
	area = img1[0:filas, 0:cols]

	# 
	img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)


	img1_fg = cv2.bitwise_and(area,area,mask = mask_inv)

	img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

	dst = cv2.add(img1_fg,img2_fg)
	img1[0:filas, 0:cols] = dst

	cv2.imshow("res", img1)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return


if __name__ == '__main__':
	main()