# -*- coding:utf-8 -*-

import numpy as np

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

if __name__ == "__main__":
    main()