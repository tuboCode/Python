# -*- coding:utf-8 -*-

import numpy as np
#导入矩阵计算模块
from numpy.linalg import *

def main():
    lst = [[1,2,3], [4,5,6]]
    #type类型
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    np_lst = np.array(lst, dtype=np.float)
    #打印形状
    print(np_lst.shape)
    #ndim维度
    print(np_lst.ndim)
    #dtype数据类型
    print(np_lst.dtype)
    #itemsize 是numpy.array中每个数据的大小
    print(np_lst.itemsize)
    #size： array中大小
    print(np_lst.size)
    print(np.zeros([2,4]))
    print(np.ones([3,5]))
    #随机数
    print("\nRandom:\n")
    #产生一个（2,4）随机序列，0-1之间
    print(np.random.rand(2,4))
    #产生一个随机数，0-1之间
    print(np.random.rand())
    print("randint")
    #为数3是产生3个数
    print(np.random.randint(1,10,3))

    #产生正太分布的随机数
    print("randn")
    print(np.random.randn(2,4))

    #产生给定选择数据的随机数
    print("choice")
    print(np.random.choice([10,20,30]))

    #产生随机beta分布
    print(np.random.beta(1,10,100))

    #arange 产生一个等差数列
    #1-10不包括11
    #5和-1是相等的
    print(np.arange(1,11).reshape(2,5))
    print(np.arange(1,11).reshape(2,-1))
    lst = np.arange(1,11).reshape(2,5)
    print(np.exp(lst))
    print(np.exp2(lst))
    print(np.sqrt(lst))
    print(np.sin(lst))
    print(np.log(lst))
    # print(np.sum(lst))

    lst = np.array([[[1,2],[3,4]],[[4,5],[5,6]],[[6,7],[7,8]]])
    #axis 代表维度
    print(lst.sum(axis=0))
    print(lst.sum(axis=1))
    print(lst.sum(axis=2))
    print(lst.max(axis=1))
    lst1 = np.array([2,3,4])

    #单位矩阵
    print(np.eye(3))
    lst = np.array([[1,2],
                    [3,4]])
    #矩阵的逆
    print(inv(lst))
    #转秩
    print(lst.transpose())
    #行列式
    print(det(lst))
    #特征值和特征向量
    print(eig(lst))
    y = np.array([[5.],[7.]])
    print(solve(lst, y))

    print("快速傅里叶变换fft")
    print(np.fft.fft(np.array([1,1,1,1,1,1,1,1])))

    print("相关系数")
    print(np.corrcoef([1,0,1],[0,2,1]))

    #生成一元函数
    print(np.poly1d([2,1,3]))

if __name__ == "__main__":
    main()