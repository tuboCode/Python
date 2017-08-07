#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.preprocessing import Imputer
# 主动生成训练和测试的模块
from sklearn.cross_validation import train_test_split
# 导入预测结果评估模块
from sklearn.metrics import classification_report

# k进邻
from sklearn.neighbors import KNeighborsClassifier
# 决策树
from sklearn.tree import DecisionTreeClassifier
# 高斯贝叶斯
from sklearn.naive_bayes import GaussianNB


def load_datasets(feature_paths, label_paths):
    """读取特征文件和标签文件列表中的内容，归并后返回
    """
    feature = np.ndarray(shape=(0, 41))
    label = np.ndarray(shape=(0, 1))
    for file in feature_paths:
        # 使用逗号分隔符读取特征数据，将问号替换标记为缺失值，文件中不包含表头
        df = pd.read_table(file, delimiter=',', na_values='?', header=None)
        # 使用平均值补全缺失值，然后将数据进行补全
        imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
        imp.fit(df)
        df = imp.transform(df)
        # 将新读入的数据合并到特征集中
        feature = np.concatenate((feature, df))

    for file in label_paths:
        # 读取标签数据，文件中不包含表头
        df = pd.read_table(file, header=None)
        # 将新读入的数据合并到标签集和中
        label = np.concatenate((label, df))

    # 将标签归整为一维向量
    label = np.ravel(label)
    return feature, label


if __name__ == '__main__':
    ''' 数据路径 '''
    featurePaths = ['A/A.feature', 'B/B.feature', 'C/C.feature', 'D/D.feature', 'E/E.feature']
    labelPaths = ['A/A.label', 'B/B.label', 'C/C.label', 'D/D.label', 'E/E.label']
    ''' 读入数据  '''
    # 将前四个数据作为训练集读入
    x_train, y_train = load_datasets(featurePaths[:4], labelPaths[:4])
    # 将最后一个作为测试数据读入
    x_test, y_test = load_datasets(featurePaths[4:], labelPaths[4:])
    # 使用全量数据作为训练集，借助train_test_split函数将训练数据打乱
    x_train, x_, y_train, y_ = train_test_split(x_train, y_train, test_size=0.0)

    print('Start training knn')
    knn = KNeighborsClassifier().fit(x_train, y_train)
    print('Training done')
    answer_knn = knn.predict(x_test)
    print('Prediction done')

    print('Start training DT')
    dt = DecisionTreeClassifier().fit(x_train, y_train)
    print('Training done')
    answer_dt = dt.predict(x_test)
    print('Prediction done')

    print('Start training Bayes')
    gnb = GaussianNB().fit(x_train, y_train)
    print('Training done')
    answer_gnb = gnb.predict(x_test)
    print('Prediction done')

    # 计算准确率与召回率
    print('\n\nThe classification report for knn:')
    print(classification_report(y_test, answer_knn))
    print('\n\nThe classification report for DT:')
    print(classification_report(y_test, answer_dt))
    print('\n\nThe classification report for Bayes:')
    print(classification_report(y_test, answer_gnb))