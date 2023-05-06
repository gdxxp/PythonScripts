import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
import base64
from alert_jpg import img as alert

img_dir = "test"

if not os.path.exists(img_dir):
    os.mkdir(img_dir)

if len(os.listdir((img_dir))) == 0:
    tmp = open('alert.jpg', 'wb')  # 创建临时的文件
    tmp.write(base64.b64decode(alert))  ##把这个one图片解码出来，写入文件中去。
    tmp.close()
    alert_img = cv2.imread('alert.jpg')
    cv2.namedWindow("warn")
    cv2.imshow("warn", alert_img)
    cv2.waitKey(1500)
    os.remove('alert.jpg')

for img_name in os.listdir(img_dir):
    imgpath = os.path.join(img_dir, img_name)
    img = cv2.imread(imgpath)
    cv2.namedWindow("cs1")
    cv2.imshow("cs1",img)
    img0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("cs2")
    cv2.imshow("cs2",img0)
    window_name = ["cs1", "cs2"]

    # 图像大小,形状
    sx = np.size(img0,0)
    sy = np.size(img0,1)
    print(sx,sy)
    print(np.shape(img0))

    # 生成三维坐标
    x = np.linspace(0, sx, sx)
    y = np.linspace(0, sy, sy)
    X, Y = np.meshgrid(y, x)
    Z = img0

    # 绘制三维surface plot
    figure = plt.figure(1, figsize = (12, 4))
    subplot3d = plt.subplot(111, projection='3d')
    surface = subplot3d.plot_surface(X, Y, Z,rstride = 5, cstride = 5,cmap = plt.get_cmap('rainbow'))
    plt.show()
