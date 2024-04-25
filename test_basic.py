#初识penCV-Python，作为了解OpenCV的使用

import cv2
import numpy

#读取图片
raw_img = cv2.imread("test.jpg")                            #无参数，目前暂不知道和 cv2.IMREAD_COLOR cv2.IMREAD_UNCHANGED的区别
#img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)         #读取灰度图片， 单通道


#img = cv2.resize(img, (1920, 1080))                        #可以改变图像的像素


#转为灰度图
img = cv2.cvtColor(raw_img, cv2.COLOR_RGB2GRAY)             #单通道8位图像


#输出图片的形状信息
print(img.shape)                                            #获取图像的形状，灰度图像返回行列，彩色图像 返回行列和通道数
print(img.dtype)                                            #获取图像深度，uint8；


#显示ROI(Region of interst)感兴趣的区域
#half = img[1512:3024,0:4032]                               #作用相当于截屏，[列，行]


#二值化
#ret1, g_thresh =  cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)    #二值化图像，输入为img灰度图，阈值127，高于阈值赋255，cv2.THRESH_BINARY现在不知道什么意思
#adp_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)     #自适应阈值，在不同区域不同光照更适用

blur = cv2.GaussianBlur(img, (5, 5), 0)                                                         #这是什么东西
ret2, gaus_thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)             #还有这个是什么东西


#Canny边缘检测
edges_img = cv2.Canny(gaus_thresh, 200, 300)
#霍夫变换
lines = cv2.HoughLinesP(edges_img, 1, numpy.pi / 180, 1, minLineLength=60, maxLineGap=5)


for x1, y1, x2, y2 in lines[0]:
    cv2.line(raw_img, (x1, y1), (x2, y2), (255, 0, 0), 2)


#imshow的窗口大小调整
cv2.namedWindow("raw_img", cv2.WINDOW_NORMAL)                   #窗口大小可以调整

cv2.namedWindow("gaus_thresh", cv2.WINDOW_NORMAL)
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
#cv2.namedWindow("test", cv2.WINDOW_FREERATIO)               #窗口大小自适应比例


cv2.imshow("raw_img", raw_img)                                #namedWindows imshow 必须同名
cv2.imshow("gaus_thresh", gaus_thresh)                        #效果最好
cv2.imshow("edges", edges_img)



#等待用户输入，关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()