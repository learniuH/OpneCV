#Basic functions that would be required quite often when we are building OpenCV projects
import cv2
import numpy as np

img = cv2.imread('test.jpg')

#定义5x5的矩阵，对象的类型是无符号整型，8bit
kernel = np.ones((5,5), np.uint8)                                                    #np.ones means we want all of the values to be one

#conventionally,we use red,green,blue,which is RGB
#but in opencv,the image convention the channels are B G R
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                      #convert 'test.jpg' into gray scale

#next function which is blurred
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)                                       #kernel must be odd number

#find the edge of our image
imgCanny = cv2.Canny(imgBlur, 440, 460)

#sometimes we are detecting an edge
#but because there is a gap or because it's not joined properly,it doesn't detect it as a proper line
#so we can increase the thickness of our edge
imgDilation = cv2.dilate(imgCanny, kernel, iterations=5)                             #iterations means how many thickness we need

#we are going to make it thinner
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.namedWindow('Gray Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Blur Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Canny Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Dialation Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Eroded Image', cv2.WINDOW_NORMAL)

cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dialation Image', imgDilation)
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)