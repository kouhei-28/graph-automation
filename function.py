import numpy as np
import matplotlib.pyplot as plt
import glob

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
    # x軸を共有するかどうか 'all' or 'none'
    x_share = 'none', 
    # 出力の際の名前
    output_name = 'out.png', 
    # 出力先のパス
    output_path = '.\\', 
    # x軸の範囲の指定、なかったらNone
    xlim = [None, None], 
    # グラフの数の指定、なかったらNone
    num_graph = None
):

    plt.rcParams["font.size"] = font_size
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['legend.frameon'] = 'False'
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['legend.frameon'] = 'True'
    plt.rcParams['legend.framealpha'] = '0.8'
    # figとaxesの初期化
    csvs = glob.glob("*.csv")
    datas = np.loadtxt(csvs[0], delimiter=',', encoding="utf-8", dtype = "float", skiprows=skiprow)
    if num_graph is None:
        num_graph = len(datas[0,:]) - 1
    fig, axes = plt.subplots(num_graph, 1, figsize=(6.4, 4.8), sharex=x_share)

    # axesが1つの場合
    if num_graph == 1:
        axes = [axes]
    
    # プロット
    for j, csv in enumerate(csvs):
        datas = np.loadtxt(csv, delimiter=',', encoding="utf-8", dtype = "float", skiprows=skiprow)
        time = datas[:,0]*x_scale
        for i in range(num_graph):
            if len(csvs) <= len(labels):
                axes[i].plot(time, datas[:,i+1]*y_scale[i] if num_graph <= len(y_scale) else datas[:,i+1], label=labels[j], linewidth= line_width)
            else:
                axes[i].plot(time, datas[:,i+1]*y_scale[i] if num_graph <= len(y_scale) else datas[:,i+1], linewidth= line_width)

    # グリッドなどの設定
    for i in range(num_graph):
        if x_share == 'all' and i == num_graph - 1:
            axes[i].set_xlabel(xlabel)
        elif x_share != 'all':
            axes[i].set_xlabel(xlabel)
        if num_graph <= len(ylabels):
            axes[i].set_ylabel(ylabels[i])
        axes[i].grid()
        axes[i].set_xlim(xlim[0] if xlim[0] else time[0], xlim[1] if xlim[1] else time[-1])
        axes[i].minorticks_on()
        axes[0].legend()

    fig.tight_layout()
    plt.savefig(output_path+output_name)

    plt.show()