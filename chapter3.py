#How to resize and crop an image?

#OpenCV convention
#in OpenCV,the x axis towards the east, the y axis towards the south
#in OpenCV function:the width conmes first,and then the height;
import cv2

img = cv2.imread('test.jpg')
#how to resize an image?
#before it, we need to know that current size fo our image
print(img.shape)                                 #the first number is the height,the second is the width,3 is the channels which is BGR

#we have to define the width first and then the height
imgResize = cv2.resize(img, (320,240))
print(imgResize.shape)

#how to crop an image
#the height comes first and then the width
imgCropped = img[0:200, 200:300]                 #define the starting point and the ending point for our width and height

#cv2.namedWindow('Image Resize', cv2.WINDOW_NORMAL)
#cv2.namedWindow('Image Cropped', cv2.WINDOW_NORMAL)

cv2.imshow('Image Resize', imgResize)
cv2.imshow('Image Cropped', imgCropped)

cv2.waitKey(0)

