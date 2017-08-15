#!-*- coding: utf-8 -*-

"""
1:建立工程导入sklearn
2：加载训练数据
3：训练神经网络
5：测试评价集
"""

import numpy as np
# 使用listdir模块，用于访问本地文件
from os import listdir
from sklearn.neural_network import MLPClassifier

# 将加载的32*32的图片矩阵展开为一列向量
def img2vector(filename):
    # 返回大小为1*1024的矩阵
    retMat = np.zeros([1024],int)
    fr = open(filename)
    lines = fr.readlines()
    for i in range(32):
        for j in range(32):
            retMat[i*32+j] = lines[i][j]
    return retMat

# 训练数据,并将样本标签转化为one-hot向量
def readDataSet(path):
    # 获取文件夹的所有数据
    fileList = listdir(path)
    # 统计需要读取文件数量
    numFiles = len(fileList)
    # 用于存放所有的数据文件
    dataSet = np.zeros([numFiles,1024],int)
    # 存放对应的标签one-hot
    hwLabels = np.zeros([numFiles,10])
    # 遍历文件
    for i in range(numFiles):
        # 获取文件名称/路径
        filepath = fileList[i]
        # 通过文件名来获取标签
        digit = int(filepath.split('_')[0])
        # 将获取的标签置1
        hwLabels[i][digit] = 1.0
        # 读取文件内容
        dataSet[i] = img2vector(path + '/' + filepath)
    return dataSet,hwLabels

# 加载训练数据
# 将训练的图片存入train_dataSet中， 对应的标签存在train_hwLabels中
train_dataSet, train_hwLabels = readDataSet('trainingDigits')

# 构建神经网络
# 设置网络的隐含层数，各隐含层神经元个数，激活函数，学习率，优化方法，最大迭次数
# 设置100个神经元的隐含层
# hidden_layer_sizes 存放的是一个元祖，表示第i层隐含层里神经元的个数
# 使用logistic激活函数和adam优化方法，并令初始学习率为0.0001
clf = MLPClassifier(hidden_layer_sizes=100,activation='logistic',
                    solver='adam',learning_rate_init=0.0001,max_iter=2000)

# 训练神经网络
# fit函数能够根据训练集及对应的标签集
# 自动设置多层感知机的输入和输出层的神经元个数
clf.fit(train_dataSet,train_hwLabels)

# 加载测试集
dataSet,hwLabels = readDataSet('testDigits')
# 使用训练好的MLP对测试集进行预测，并计算错误率
# 对测试集进行预测
res = clf.predict(dataSet)
# 统计错误数目
error_num = 0
# 测试集的数目
num = len(dataSet)
# 遍历测试结果
for i in range(num):
    # 比较产长度为10的数组，返回包含01的数目，0为不同，1为相同
    # 若预测结果与真实结果相同，则10个数全为1， 否则不全为1
    if np.sum(res[i] == hwLabels[i]) < 10:
        error_num += 1
print("Total num:",num,"Wrong num",
      error_num,"WrongRate:", error_num/float(num))