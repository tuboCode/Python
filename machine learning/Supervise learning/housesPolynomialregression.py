#!-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

# 读取数据集
datasets_X = []
datasets_Y = []
# 读取数据
fr = open('prices.txt', 'r')
# readlines一次读取整个文件
lines = fr.readlines()
# 逐好难过进行操作，遍历所有数据
for line in lines:
    # 去除数据文件中的逗号
    items = line.strip().split(',')
    # 将读取的数据转换为int类型，并分别写入x与y中
    datasets_X.append(int(items[0]))
    datasets_Y.append(int(items[1]))
# datasets_x的长度
length = len(datasets_X)
# 将datasets_X转化为数组，并变为二维，已符合线性回归拟合函数输入参数的要求
datasets_X = np.array(datasets_X).reshape([length, 1])
# 将datasets_y转化为数组
datasets_Y = np.array(datasets_Y)

minX = min(datasets_X)
maxX = max(datasets_X)
# 从min到max建立等差数列,方便画图
X = np.arange(minX, maxX).reshape([-1, 1])

# degree=2表示建立datasrts_x的二次多项式特征X_poly
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(datasets_X)
# 创建线性回归，使用线性模型学习X_poly和datasets_Y之间的线性关系
lin_reg_2 = linear_model.LinearRegression()
lin_reg_2.fit(X_poly,datasets_Y)

# 图像中显示
plt.scatter(datasets_X, datasets_Y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()