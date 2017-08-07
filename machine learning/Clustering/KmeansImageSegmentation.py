# -*- coding: utf-8 -*-
#!/usr/local/python

import numpy as np
# 加载PIL包， 用于加载创建图片
import PIL.Image as image
# 加载KMeans
from sklearn.cluster import KMeans

def load_Data(filepath):
    # 以二进制形式打开图片
    f = open(filepath, 'rb')
    # 以列表形式返回图片像素值
    data = []
    img = image.open(f)
    # 获得图片的大小
    m,n = img.size
    # 将每个像素点的RGB颜色处理到0-1范围内并放进data
    for i in range(m):
        for j in range(n):
            x, y, z = img.getpixel((i,j))
            data.append([x/256.0,y/256.0,z/256.0])
    f.close()
        # 以矩阵形式返回data，以及图片大小
    return np.mat(data),m,n


# 加载数据
imgData,row,col = load_Data('./bull.jpg')

# 加载Kmeans聚类算法,n_clusters属性指定了聚类中心的个数为3
km = KMeans(n_clusters=3)
# 聚类获得每个像素所属的类别
label = km.fit_predict(imgData)
label = label.reshape([row, col])
# 创建一张新的灰度图保存聚类后的结果
pic_new = image.new('L', (row, col))
# 根据所属类别向图片中添加灰度值
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i,j), int(256/(label[i][j]+1)))
# 以JPEG格式保存图像
pic_new.save("result-bull-4.jpg", "JPEG")