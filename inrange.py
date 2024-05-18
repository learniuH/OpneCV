import cv2
import numpy 

# Initialize the mask as a global variable
mask = None

def inrangeThreshold(_):
    global mask
    # Correctly get the trackbar positions
    lower_h = cv2.getTrackbarPos('lower_h', 'TrackBars')
    lower_s = cv2.getTrackbarPos('lower_s', 'TrackBars')
    lower_v = cv2.getTrackbarPos('lower_v', 'TrackBars')

    upper_h = cv2.getTrackbarPos('upper_h', 'TrackBars')
    upper_s = cv2.getTrackbarPos('upper_s', 'TrackBars')
    upper_v = cv2.getTrackbarPos('upper_v', 'TrackBars')

    # Define the lower and upper bounds for the color range
    lower_bound = (lower_h, lower_s, lower_v)
    upper_bound = (upper_h, upper_s, upper_v)

    # Apply the inRange function to get the mask
    mask = cv2.inRange(hsvimage, lower_bound, upper_bound)

# Create trackbar window
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)

# Load and preprocess the image
img = cv2.imread('test.jpg')
img = cv2.resize(img, (320, 240))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 创建一个5行5列的数组
kernel = numpy.ones((5,5),numpy.uint8)
# 对图片进行膨胀腐蚀操作
hsvimage_erode = cv2.erode(hsv,kernel,iterations=1)
hsvimage = cv2.dilate(hsvimage_erode,kernel,iterations=1)

# Create the trackbars
cv2.createTrackbar('lower_h', 'TrackBars', 0, 255, inrangeThreshold)
cv2.createTrackbar('lower_s', 'TrackBars', 0, 255, inrangeThreshold)
cv2.createTrackbar('lower_v', 'TrackBars', 51, 255, inrangeThreshold)
cv2.createTrackbar('upper_h', 'TrackBars', 155, 255, inrangeThreshold)
cv2.createTrackbar('upper_s', 'TrackBars', 9, 255, inrangeThreshold)
cv2.createTrackbar('upper_v', 'TrackBars', 162, 255, inrangeThreshold)

# Call inrangeThreshold initially to define mask
inrangeThreshold(None)

while True:
    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)

    if mask is not None:
        cv2.imshow('mask', mask)

    if cv2.waitKey(1) & 0xFF == 27:  # Exit loop on 'Esc' key
        break

cv2.destroyAllWindows()