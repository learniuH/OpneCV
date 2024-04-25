#用于确定Canny函数的上下阈值，并在窗口中显示
#目前的bug：窗口过大，没法调整大小；
#另外的一个想法：通过调整图像的像素，可否可以优化边缘检测的效果（目前的边缘检测效果并不好）
import cv2

img_path = 'test.jpg'                                                                      #存放图像的路径
img_tmp = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)                                       #读取灰度图，用于边缘检测
edges = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)                                         
minThreshold = 0                                                                           #下阈值
maxThreshold = 0                                                                           #上阈值

def updateminThreshold(x):                                                                 #更新边缘检测下阈值
    global minThreshold,edges
    minThreshold = cv2.getTrackbarPos('minThreshold', 'edge_detection')                    #获取 滑动条的数值 = (滑动条的名字，滑动条所在窗口)
    edges = cv2.Canny(img_tmp, minThreshold, maxThreshold)                                 #边缘检测

def updatemaxThreshold(x):                                                                 #更新边缘检测上阈值
    global maxThreshold,edges
    maxThreshold = cv2.getTrackbarPos('maxThreshold', 'edge_detection')
    edges = cv2.Canny(img_tmp, minThreshold, maxThreshold)

cv2.namedWindow('edge_detection', cv2.WINDOW_NORMAL)
#绑定滑动条和窗口，定义滑动条的数值
cv2.createTrackbar('minThreshold', 'edge_detection', 400, 1000, updateminThreshold)        #(滑动条的名字，滑动条被放置窗口的名字，滑动条默认值，滑动条最大值，回调函数)
cv2.createTrackbar('maxThreshold', 'edge_detection', 500, 1000, updatemaxThreshold)        #回调函数更新两个阈值

while (True):
    cv2.imshow('edge_detection', edges)
    if cv2.waitKey(1) == ord('q'):                                                         #键盘输入小写q可退出 
        break
cv2.destroyAllWindows()

