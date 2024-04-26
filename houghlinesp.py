import cv2
import numpy as np

def calculate_slope(line):
    #计算line的斜率
    x1,y1,x2,y2 = line[0]
    return (y2-y1) / (x2-x1)

edges_img = cv2.imread('masked_gaus_edges_img.jpg', cv2.IMREAD_GRAYSCALE)
#获取所有线段
lines = cv2.HoughLinesP(edges_img, 1, np.pi / 180, 15, minLineLength=100, maxLineGap=20)
#按照斜率分成左右边界
#斜率大于1（45°以上）归为左边界
#斜率小于-1（90°~135°）归为右边界
left_lines = [line for line in lines if calculate_slope(line) > 1]                      #列表方程式，Python语法
right_lines = [line for line in lines if calculate_slope(line) < -1]                    #for line in lines 循环lines里的每条线，判断斜率，然后分为左右两类

#print('before filter:')
#print('all filter:', len(lines))                                                        #一共识别到2398条线
#print('left filter:', len(left_lines))                                                  #左边有246条
#print('right filter:', len(right_lines))                                                #右边有110条

#离群值过滤：
#左右边界直线的斜率是大致相同的
#需要把斜率误差过大的直线过滤掉
def reject_abnormal_lines(lines, threshold):
    #删除斜率不一致的线段
    slopes = [calculate_slope(line) for line in lines]
    while len(lines) > 0:
        mean = np.mean(slopes)                                                          #计算所有斜率的平均值
        diff = [abs(s - mean) for s in slopes]                                          #计算每条直线斜率与平均斜率的差值
        idx = np.argmax(diff)                                                           #找到差值最大的线段的下标
        if diff[idx] > threshold:
            slopes.pop(idx)                                                             #在slopes里删除这条直线
            lines.pop(idx)                                                              #在lines里删除这条直线
        else:
            break
    return lines

reject_abnormal_lines(left_lines, threshold=0.2)
reject_abnormal_lines(right_lines, threshold=0.2)

#print('after filter:')
#print('right filter:', len(right_lines))                                              #右边有35条
#print('left filter:', len(left_lines))                                                #左边有115条

#最小二乘拟合
def least_squares_fit(lines):
    #将lines中线段拟合成一条直线
    #1.取出所有坐标点
    x_coords = np.ravel([[line[0][0], line[0][2]] for line in lines])                 #取出直线对应的x坐标
    y_coords = np.ravel([[line[0][1], line[0][3]] for line in lines])                 #取出直线对应的y坐标
    #2.进行直线拟合，得到多项式系数
    poly = np.polyfit(x_coords, y_coords, deg=1)                                      #deg=1 拟合成一次直线
    #3.根据多项式系数，计算两个直线上的点，用于唯一确定这条直线
    point_min = (np.min(x_coords), np.polyval(poly, np.min(x_coords)))
    point_max = (np.max(x_coords), np.polyval(poly, np.max(x_coords)))
    return np.array([point_min, point_max], dtype=np.int32)

print(least_squares_fit(left_lines))
print(least_squares_fit(right_lines))

left_line = least_squares_fit(left_lines)
right_line = least_squares_fit(right_lines)

img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
#绘制两条直线
cv2.line(img, tuple(left_line[0]), tuple(left_line[1]), color=(255, 0, 255), thickness=20)
cv2.line(img, tuple(right_line[0]), tuple(right_line[1]), color=(255, 0, 255), thickness=20)

cv2.namedWindow('result', cv2.WINDOW_NORMAL)
#cv2.imwrite('result.jpg', img)
cv2.imshow('result', img)
cv2.waitKey()