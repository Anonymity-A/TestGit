# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.axisartist.axislines import AxesZero
from mpl_toolkits.axisartist.axis_artist import AxisArtist


if __name__ == "__main__":
    # data for drawing
    x: list[int] = [i+1 for i in range(10)]
    y: list[int] = [0, 992134, 1537614, 245326, 238763, 0, 319765, 0, 62319, 0]

    # setting for drawing
    # 坐标轴、字体、字号设置
    parameters: dict = {'font.sans-serif': ['Times New Roman'],
                        'axes.labelsize': 28,
                        'axes.titlesize': 30,
                        'xtick.labelsize': 24,
                        'ytick.labelsize': 24,
                        'legend.fontsize': 24}
    # x tick label
    strTickLabel: list[str] = ["celling", "floor", "wall",
                               "table", "chair", "person",
                               "plant", "sofa", "tvmonitor", "clutter"]
    # legend label
    strLegendLabel: list[str] = ["_celling", "floor", "wall",
                                 "table", "chair", "_person",
                                 "plant", "_sofa", "tvmonitor", "_clutter"]
    # color of bar
    strBarColors: list[str] = ['#104680', '#317CB7', '#6DADD1',
                               '#B6D7E8', '#E9F1F4', '#FBE3D5',
                               '#F6B293', '#DC6D57', '#B72230', '#6D011F']
    plt.rcParams.update(parameters)

    # start...
    # 申请画板: fig (1920*1080)
    fig: Figure = plt.figure(figsize=(19.2, 10.8))
    # 从fig中申请一张画纸: axesMain
    axesMain: AxesZero = fig.add_subplot(axes_class=AxesZero)  # plt.axes()
    # 在axMain画纸上绘制柱状图
    axesMain.bar(x, y,
                 tick_label=strTickLabel,
                 label=strLegendLabel,
                 color=strBarColors)
    # 设置x轴名称
    axesMain.set_xlabel("scences")
    # 设置y轴名称
    axesMain.set_ylabel('count')
    # 设置标题名称
    axesMain.set_title('Label classification histogram')
    # 设置图例名称 axMain.legend(title='Scenes')
    # 显示图例
    axesMain.legend()
    # 显示网格
    axesMain.grid(linestyle='--')
    # 设置坐标轴
    axisHandleTop: AxisArtist = axesMain.axis["top"]
    axisHandleBotton: AxisArtist = axesMain.axis["bottom"]
    axisHandleLeft: AxisArtist = axesMain.axis["left"]
    axisHandleRight: AxisArtist = axesMain.axis["right"]
    axisHandleTop.set_visible(False)
    axisHandleBotton.set_axisline_style("-|>", size=1.5)
    axisHandleLeft.set_axisline_style("-|>", size=1.5)
    axisHandleRight.set_visible(False)

    # 调整边界
    plt.subplots_adjust(top=0.91, bottom=0.08,
                        left=0.05, right=0.95,
                        wspace=0.2, hspace=0.2)
    # 保存图片
    plt.savefig("./output/Save.png")
    # 展示画板？画纸
    plt.show()
    pass
