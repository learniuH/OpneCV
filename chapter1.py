#How to use a webcam?
import cv2 

#write of the id of our camera,if you just have one webcam or you have a laptop connected
#so you can press 0,and this will use the default webcam.
cap = cv2.VideoCapture(0)                                               #获取摄像头的图像
#define some parameter for it
cap.set(3, 640)                                                         #id：3 - 定义指定的宽度
cap.set(4, 480)                                                         #id：4 - 定义指定的高度
cap.set(10, 100)                                                        #id: 10 - 定义指定亮度

while True:
    success, img = cap.read()                                           #将图像保存到img中，并可以判断是否成功
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):                               # waitKey 0:无限延迟，非0的单位是ms
        break