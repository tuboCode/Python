#! -*- coding: utf-8 -*-

from sklearn.cluster import KMeans
import numpy as np

def LoadData(filepath):
    """
    :param filepath: 文件路径
    :return: retData 存储城市的各项信息
    :return: retCityName 存储城市名称
    """

    fr = open(filepath, 'r+')
    # """
    # readlines 一次读取整个文件
    # readline 一次读取一行，比readlines慢点多。没有足够
    # 内存就用 readline()
    # """
    lines = fr.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.strip().split(",")
        retCityName.append(items[0])
        retData.append([float(items[i]) for i in range(1,len(items))])

    #for i in range(1, len(items)):
    return retData, retCityName



if __name__ == '__main__':
    #
    # """
    # n_clusters: 用于指定聚类中心的距离
    # init: 初始聚类中心的初始化方法
    # max_iter :最大的迭代次数
    # 一般用的时候只给出 n_cluster 即可， init 默认时init为k-means++, max_iter为300
    # data :加载的数据
    # label :聚类后各类数据所属的标签
    # axis :按行求和
    # fit_predict() :计算中心以及簇分配序号
    # """
    data, cityName = LoadData('city.txt')
    km = KMeans(n_clusters=4)
    label = km.fit_predict(data)
    expenses = np.sum(km.cluster_centers_, axis=1)
    print(expenses)
    CityCluster = [[], [], [], []]
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])
    for i in range(len(CityCluster)):
        print("Expenses:%.2f" % expenses[i])
        print(CityCluster[i])
