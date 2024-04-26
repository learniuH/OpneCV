
#test.jpg梯形：左下(0,2200)   左上(1000,900)  右上(3000,900)  右下(4032,2200)
#test.jpg下半部分矩形：右下(4032,3024)  左下(0,3024)

import cv2
import numpy as np

#测试图片的路径
img_path = 'test.jpg'
#边缘检测参数
minThreshold = 440
maxThreshold = 460
#fillPoly函数的参数，梯形的坐标
rectangular = np.array([[0, 2200], [1000, 900], [3000, 900], [4032, 2200], [4032, 3024], [0, 3024]])


gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
#高斯滤波
gaus_img = cv2.GaussianBlur(gray_img, (5, 5), 0)                                                          

#edge_detection
edge_img = cv2.Canny(gaus_img, minThreshold, maxThreshold)
#图像掩码
mask = np.zeros_like(edge_img)                                                              #获取一个与edge_img大小相同的numpy数组，每一位都是0
mask = cv2.fillConvexPoly(mask, rectangular, color=255)                                     #单个多边形填充
#获取掩码图像
masked_deges_img = cv2.bitwise_and(edge_img, mask)

cv2.namedWindow('masked_deges_img', cv2.WINDOW_NORMAL)
#cv2.imwrite('masked_gaus_edges_img.jpg', masked_deges_img)                                      #保存图片
cv2.imshow('masked_deges_img', masked_deges_img)
cv2.waitKey()
cv2.destroyAllWindows()