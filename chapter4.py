#How to draw shapes on images?
#learn how to draw lines rectangles circls and also learn how to put text on images.
import cv2
import numpy as np

#create a matrix filled with zeros
#img = np.zeros((512, 512))
#print(img.shape)

#this gives us the values from 0 to 255
img = np.zeros((512,512,3), np.uint8)
print(img.shape)

#how we can color this image?
#the colored part is only the rang that we have defined,and the color is blue;
#if we want color whole image,we could just write a :
#img[200:300, 100:300] = 255, 0, 0  

#how to create a line?
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), thickness=3)         #(starting point,ending point,line color,thickness)
#how to create a rectangles?
#if you want to fill the entire rectangle,just replace the 3 with cv2.FILLED
cv2.rectangle(img, (0,0), (250,350), (0,0,255), 3)
#how to create a circle?
cv2.circle(img, (256,256), 50, (255,255,0), 5)

#how to put text on images?
#                   text          start pont                         SCALE   color   thickness
cv2.putText(img, "OpenCV-Python", (100, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (150,150,0), 3)

cv2.imshow('Image', img)

cv2.waitKey(0)