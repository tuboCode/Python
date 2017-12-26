import matplotlib.pyplot as plt
import numpy as np


def main():
    # -pi到pi之间包含256个点，包含最后一个点,类似matlab
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # 定义余弦函数与正弦函数
    c, s = np.cos(x), np.sin(x)
    # 绘图
    plt.figure(1)
    # lineweight :线宽 linestyle ：线的风格 lable：标签 alpha：透明度
    plt.plot(x, c, color="blue", linewidth=1, linestyle="-", label="cos", alpha=0.5)
    # r* : 代表 红色的心
    plt.plot(x, s, "r*", label="sin")
    # 加一个标题
    plt.title("cos & sin")
    # 轴的编辑器
    ax = plt.gca()
    # spines 图的轴线
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    # xticks两个数组， 第一个数组标示横轴标识记得位置， 第二个数组标示标识的内容
    plt.xticks([-np.pi, np.pi / 2, 0, np.pi / 2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    # 设置字体 得到横轴和纵轴的label
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        # 设置字体大小
        label.set_fontsize(16)
        # 设置label box大小
        label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2))
    # legend 图例
    plt.legend(loc="upper left")
    # 网格线
    plt.grid()
    # 通过axis来限制显示范围 前两个数为x范围 ，后两个为y的范围
    # plt.axis([-1,1,-0.5,1])


    # 填充 前两个数为x条件，后两个为y的条件
    plt.fill_between(x, np.abs(x) < 1, c, c > 0.5, color='green', alpha=0.25)

    # 注释
    t = 2
    plt.plot([t, t], [0, np.cos(t)], 'y', linewidth=3, linestyle='--')
    # 添加注释
    # textcoords="offset points" 指定相对位置
    # arrowstyle 箭头属性
    plt.annotate("cos(2)", xy=(t, np.cos(2)), xycoords="data", xytext=(+10, +30),
                 textcoords="offset points", arrowprops=dict(arrowstyle="->",
                                                             connectionstyle="arc3,rad=.5"))
    plt.show()


if __name__ == '__main__':
    main()
