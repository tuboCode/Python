#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#数据可视化
import matplotlib.pyplot as plt
# 加载PCA算法包
from sklearn.decomposition import PCA
# 加载鸢尾花数据集导入函数
from sklearn.datasets import load_iris

# 以字典形式加载数据
data = load_iris()
# y 表示数据集中的标签
y = data.target
# x 表示数据集中的属性数据
X = data.data
# 加载PCA算法，设置降维后主成分数目为2
pca = PCA(n_components=2)
# 对原始数据进行进行降维，保存到reduced_X中
reduced_X = pca.fit_transform(X)

"""
数据点
"""
red_x, red_y = [],[]
blue_x, blue_y = [],[]
green_x, green_y = [],[]

"""
按照鸢尾花的类别将降维后的数据保存到不同的列表中
"""
# print(reduced_X)
for i in range(len(reduced_X)):
    if y[i] == 0:
        red_x.append(reduced_X[i][0])
        red_y.append(reduced_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_X[i][0])
        blue_y.append(reduced_X[i][1])
    else:
        green_x.append(reduced_X[i][0])
        green_y.append(reduced_X[i][1])


# 可视化
plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y ,c='g', marker='.')

plt.show()