#!/uer/local/bin/ python
# -*- coding: utf-8 -*-

# 数据可视化
import matplotlib.pyplot as plt
# 加载PCA算法
from sklearn import decomposition
# 加载 RandomState 创建随机种子
from numpy.random import RandomState
# 加载olivetti人脸数据集导入图像
from sklearn.datasets import fetch_olivetti_faces


# 图像排列情况 2行3列
n_row, n_col = 2,3
# 设置提取的特征值数目
n_components = n_row * n_col
# 设置人脸数据图片的大小
image_shape = (64, 64)

# 加载数据集， 并打乱顺序
dataset = fetch_olivetti_faces(shuffle=True, random_state=RandomState(0))
faces = dataset.data

def plot_gallery(title, images, n_col=n_col, n_row=n_row):
    # 创建图片， 并指定图片大小（英寸）
    plt.figure(figsize=(2. * n_col, 2.26 * n_row))
    # 设置标题和字号大小
    plt.suptitle(title, size=16)

    for i, comp in enumerate(images):
        # 选择画制的子图
        plt.subplot(n_row, n_col, i+1)
        vmax = max(comp.max(), -comp.min())
        # 对数值归一化并以灰度图形式显示
        plt.imshow(comp.reshape(image_shape), cmap=plt.cm.gray,
                   interpolation='nearest',vmin=-vmax, vmax=vmax)
        # 去除子图坐标轴标签
        plt.xticks(())
        plt.yticks(())
    # 对子图位置及间距调整
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.94, 0.04, 0.)

plot_gallery("First cnetered Olivetti faces", faces[:n_components])

# 创建特征提取的对象NMF, 使用PCA作为对比
estimators = [
    ('Eigenfaces - PCA using randomized SVD',
     decomposition.PCA(n_components=6,whiten=True)),
    ('Non-nagative components - NMF',
     decomposition.NMF(n_components=6, init='nndsvda',tol=5e-3))
]

# 分别调用PCA和NMF
for name, estimator in estimators:
    print("Extractoing the top %d %s ..." % (n_components, name))
    print(faces.shape)
    # 调用PCA或NMF提取特征
    estimator.fit(faces)
    # 获取提取的特征
    components_ = estimator.components_
    # 按照固定格式进行排列
    plot_gallery(name, components_[:n_components])

plt.show()

