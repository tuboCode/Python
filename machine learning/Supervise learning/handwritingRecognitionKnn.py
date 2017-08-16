# -*- coding: utf-8 -*-

import numpy as np
from os import listdir
from sklearn import neighbors

def img2vector(filename):
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

train_dataSet, train_hwLabels = readDataSet('trainingDigits')
knn = neighbors.KNeighborsClassifier(algorithm='kd_tree',n_neighbors=3)
knn.fit(train_dataSet,train_hwLabels)

test_dataSet, test_hwLabels = readDataSet('testDigits')

res = knn.predict(test_dataSet)
err_num = np.sum(res != test_hwLabels)
num = len(test_dataSet)
print("Total num:",num," Wrong num:", err_num,"  WrongRate:",err_num / float(num))