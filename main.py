# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# import opencv-draw-tools-fera as cv2_tools
import cv2
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    image = cv2.imread('./m21.jpg')
    cv2.imshow('image', image)

    # 构造卷积核
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    # 常用卷积核
    # 1.低通滤波器
    lowFilter1 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) * (1 / 9)
    lowFilter2 = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]]) * (1 / 10)
    lowFilter3 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) * (1 / 16)
    # 2.高通滤波器
    highFilter1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    highFilter2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    highFilter3 = np.array([[1, -2, 1], [-2, 5, -2], [1, -2, 1]])
    # 3.平移和差分边缘检测
    moveFilter1 = np.array([[0, 0, 0], [-1, 1, 0], [0, 0, 0]])
    moveFilter2 = np.array([[0, -1, 0], [0, 1, 0], [0, 0, 0]])
    moveFilter3 = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]])
    # 4.匹配滤波边缘检测
    pipeiedgFilter1 = np.array([[-1, -1, -1, -1, -1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]])
    pipeiedgFilter2 = np.array([[-1, 0, -1], [-1, 0, -1], [-1, 0, -1], [-1, 0, -1], [-1, 0, -1]])
    # 5.边缘检测
    edgeFilter1 = np.array([[-1, 0, -1], [0, 4, 0], [-1, 0, -1]])
    edgeFilter2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    edgeFilter3 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    edgeFilter4 = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
    # 6.梯度方向检测
    tiduFilter1 = np.array([[1, 1, 1], [1, -2, 1], [-1, -1, -1]])
    tiduFilter2 = np.array([[1, 1, 1], [-1, -2, 1], [-1, -1, 1]])
    tiduFilter3 = np.array([[-1, 1, 1], [-1, -2, 1], [-1, 1, 1]])
    tiduFilter4 = np.array([[-1, -1, 1], [-1, -2, 1], [1, 1, 1]])

    tiduFilter5 = np.array([[-1, -1, -1], [1, -2, 1], [1, 1, 1]])
    tiduFilter6 = np.array([[1, -1, -1], [1, -2, -1], [1, 1, 1]])
    tiduFilter7 = np.array([[1, 1, -1], [1, -2, -1], [1, 1, -1]])
    tiduFilter8 = np.array([[1, 1, 1], [1, -2, -1], [1, -1, -1]])

    # 卷积计算
    # dst = cv2.filter2D(image, -1, kernel)
    dst = cv2.filter2D(image, -1, tiduFilter8)

    # 显示计算之后的图片
    cv2.imshow('dst', dst)
    # 保存图片
    cv2.imwrite('./mtiduFilter8.jpg', dst)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# python 3.5.3
# 2017-03-09 蔡军生  http://blog.csdn.net/caimouse
#


# 读取图片并显示
