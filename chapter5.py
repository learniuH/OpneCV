#detect the color in the image
import cv2
import numpy as np

def empty(a):
    pass

img = cv2.imread('test.jpg')

#create window
cv2.namedWindow('TrackBars')
#resize window
cv2.resizeWindow('TrackBars', 640, 240)
#create the track bar
cv2.createTrackbar('HUE MIN','TrackBars', 0, 179, empty)
cv2.createTrackbar('HUE MAX','TrackBars', 179, 179, empty)
cv2.createTrackbar('SAT MIN','TrackBars', 0, 255, empty)
cv2.createTrackbar('SAT MAX','TrackBars', 255, 255, empty)
cv2.createTrackbar('VAL MIN','TrackBars', 0, 255, empty)
cv2.createTrackbar('VAL MAX','TrackBars', 255, 255, empty)

imgResize = cv2.resize(img, (320,240))

imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)

while True:
    #get the tarck bar values so we can apply on our image
    h_min = cv2.getTrackbarPos('HUE MIN','TrackBars')                   #tarckbar name, window name
    h_max = cv2.getTrackbarPos('HUE MAX','TrackBars')
    s_min = cv2.getTrackbarPos('SAT MIN','TrackBars')
    s_max = cv2.getTrackbarPos('SAT MAX','TrackBars')
    v_min = cv2.getTrackbarPos('VAL MIN','TrackBars')
    v_max = cv2.getTrackbarPos('VAL MAX','TrackBars')
    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    
    #orignal image we want to use,and our new image will be also like our orignal image but with a mask applied
    imgResult = cv2.bitwise_and(imgResize, imgResize, mask=mask)

    cv2.imshow('Image Resize', imgResize)
    cv2.imshow('HSV', imgHSV)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', imgResult)

    cv2.waitKey(1)  #如果是0，将无休止的延迟下去，也就不会print，所以改成1，循环才继续