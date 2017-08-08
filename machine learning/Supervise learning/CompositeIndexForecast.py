#-*- coding: utf-8 -*-
#/usr/bin/local/python

import numpy as np
import pandas as pd
# SVM 算法
from sklearn import svm
# sklearn下cross_validation：交叉验证
from sklearn import cross_validation

# 加载数据
data = pd.read_csv('000777.csv', encoding='gbk',parse_dates=[0],index_col=0)
# sort_index按照时间生序排列
data.sort_index(0,ascending=True,inplace=True)

# dayfeature: 选取150天的数据
dayfeature = 150
# featurenum: 选取的5个特征*天数
featurenum = 5*dayfeature

"""
data.shape[0]-dayfeature意思是因为我们要用150天的数据做训练，对于条目
为200条的数据，只有50条数据是目前150的数据来寻来训练的，所以训练集的大小
就是200-150， 对于每一条数据，他的特征值是前150天所有特征数据，即150*5
+1 是将当天的开盘价引入作为一条特征数据

"""
# x:记录150天的5个特征数据
x=np.zeros((data.shape[0]-dayfeature, featurenum+1))
# y:记录涨或跌
y=np.zeros((data.shape[0]-dayfeature))

# 数据预处理
for i in range(0,data.shape[0]-dayfeature):
    x[i,0:featurenum]=np.array(data[i:i+dayfeature] \
          [[u'收盘价',u'最高价',u'最低价',u'开盘价',u'成交量']]).reshape((1,featurenum))
    # 将数据中的收盘价，最高价，开盘价，成交量 存入x数组中
    x[i,featurenum]=data.ix[i+dayfeature][u'开盘价']

# 最后一列记录当天的开盘价
for i in range(0,data.shape[0]-dayfeature):
    # 如果当天收盘价高于开盘价，y[i]=1代表涨， 0代表跌
    if data.ix[i+dayfeature][u'收盘价']>=data.ix[i+dayfeature][u'开盘价']:
        y[i]=1
    else:
        y[i]=0

# 创建SVM进行交叉认证
clf = svm.SVC(kernel='rbf')
# 调用svm函数并并设置kernel参数，默认是rbf, 其他是：linear, poly, sigmoid
result = []
for i in range(5):
    # x和y的验证集和测试集， 切分80%-20%的测试集
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    # 训练数据进行训练
    clf.fit(x_train, y_train)
    # 将预测数据和测试数据的验证数据比对
    result.append(np.mean(y_test == clf.predict(x_test)))
    print("svm classifier accuacy")
    print(result)
