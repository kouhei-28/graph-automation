import function
import json

json_open = open('original.json', 'r')
json_load = json.load(json_open)

function.output_graph(**json_load)

# function.output_graph(
#     ############################## 各種パラメータの設定 ############################################
#     # フォントサイズ
#     font_size = 16, 
#     # データの何行目まで飛ばすか
#     skiprow = 1, 
#     # 線の太さ
#     line_width = 2.0, 
#     # xラベルの名称
#     xlabel = r'Time [ns]', 
#     # yラベルの名称
#     ylabels = [], 
#     # 凡例ラベルの名称
#     labels = [], 
#     # x軸の値の倍率
#     x_scale = 1, 
#     # y軸の値の倍率
#     y_scale = [1, 1, 1e-3], 
#     # x軸を共有するかどうか 'all' or 'none'
#     x_share = 'none', 
#     # 出力の際の名前
#     output_name = 'out.png', 
#     # 出力先のパス
#     output_path = '.\\', 
#     # x軸の範囲の指定、なかったらNone
#     xlim = [None, None], 
#     # グラフの数の指定、なかったらNone
#     num_graph = None
#     #############################################################################################
# )