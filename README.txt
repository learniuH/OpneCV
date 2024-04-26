将图片放在根目录，不要修改图片名字/后缀！！！

1.edge_detection.py：是一个小程序（制作了一个窗口，可以在窗口内改变边缘检测的上下阈值，并通过窗口反映出来），用于查看Canny边缘检测的效果
2.roi_mask.py：对 test.jpg 进行图像处理（使用高斯滤波对图像进行模糊处理，使用Canny函数进行边缘检测，然后对图像中进行了掩码处理，获取感兴趣的部分），得到边缘检测后的感兴趣的图像 masked_gaus_edges_img.jpg
3.houghlinesp.py：使用上面得到的 masked_gaus_edges_img.jpg 进行霍夫变换，得到图像中的线段，对这些线段进行处理（离群值过滤、最小二乘拟合），最终得到两条边界线，效果图是 result.jpg
