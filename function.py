import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd

# プロット
def plot(axes, datas, time, display_graph, labels, y_scale, line_width, j, length):
    for k, i in enumerate(display_graph):
        if length <= len(labels):
            axes[k].plot(time, datas[:,i]*y_scale[i-1] if len(display_graph) <= len(y_scale) else datas[:,i], label=labels[j], linewidth= line_width)
        else:
            axes[k].plot(time, datas[:,i]*y_scale[i-1] if len(display_graph) <= len(y_scale) else datas[:,i], linewidth= line_width)

# グラフの体裁を整える
def format_graph(axes, time, display_graph, xlabel, ylabels, xlim, legend_posi):
    axes[-1].set_xlabel(xlabel)
    for k, i in enumerate(display_graph):
        if len(display_graph) <= len(ylabels):
            axes[k].set_ylabel(ylabels[k])
        axes[k].grid()
        axes[k].set_xlim(xlim[0] if xlim[0] else time[0], xlim[1] if xlim[1] else time[-1])
        axes[k].minorticks_on()
        if legend_posi == k:
            axes[k].legend()


def output_graph(
    # フォントサイズ
    font_size = 16, 
    # データの何行目まで飛ばすか
    skiprow = 1, 
    # 線の太さ
    line_width = 2.0, 
    # xラベルの名称
    xlabel = r'Time [ns]', 
    # yラベルの名称
    ylabels = [], 
    # 凡例ラベルの名称
    labels = [], 
    # x軸の値の倍率
    x_scale = 1, 
    # y軸の値の倍率
    y_scale = [], 
    # 出力の際の名前
    output_name = 'out.png', 
    # 出力先のパス
    output_path = '.\\', 
    # x軸の範囲の指定、なかったらNone
    xlim = [None, None], 
    # グラフの高さを指定
    height = 1, 
    # グラフの幅を指定
    width = 1, 
    # 凡例の位置
    legend_posi = 0,
    # 表示するグラフの選択
    display_graph = [1]
):

    plt.rcParams["font.size"] = font_size
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['legend.frameon'] = 'False'
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['legend.frameon'] = 'True'
    plt.rcParams['legend.framealpha'] = '0.8'

    # datas = select_display_graph(display_graph, skiprow)
    
    # figとaxesの初期化
    fig, axes = plt.subplots(len(display_graph), 1, figsize=(6.4*width, 4.8*height), sharex=True)
    # axesが1つの場合
    if len(display_graph) == 1:
        axes = [axes]

    # if glob.glob("~$*.xlsx"):
    #     print("Please close Excel file. ")
    #     return

    if glob.glob("*.csv"):
        csvs = glob.glob("*.csv")
        for j, csv in enumerate(csvs):
            datas = np.loadtxt(csv, delimiter=',', encoding="utf-8", dtype = "float", skiprows=skiprow)
            time = datas[:,0]*x_scale
            plot(axes, datas, time, display_graph, labels, y_scale, line_width, j, length=len(csvs))

    if glob.glob("*.txt"):
        txts = glob.glob("*.txt")
        for j, txt in enumerate(txts):
            datas = np.loadtxt(txt, delimiter=',', encoding="utf-8", dtype = "float", skiprows=skiprow)
            time = datas[:,0]*x_scale
            plot(axes, datas, time, display_graph, labels, y_scale, line_width, j, length=len(txts))

    if glob.glob("*.xlsx"):
        xlsxs = glob.glob("*.xlsx")
        for j, xlsx in enumerate(xlsxs):
            if "~$" in xlsx:
                continue
            for i in range(len(pd.ExcelFile(xlsx).sheet_names)):
                datas = pd.ExcelFile(xlsx).parse(pd.ExcelFile(xlsx).sheet_names[i]).to_numpy()
                time = datas[:,0]*x_scale
                plot(axes, datas, time, display_graph, labels, y_scale, line_width, j, length=len(xlsxs))
    
    # グラフの体裁を整える
    format_graph(axes, time, display_graph, xlabel, ylabels, xlim, legend_posi)

    # layoutを整える
    fig.tight_layout()
    # グラフの保存と表示
    plt.savefig(output_path+output_name)
    plt.show()