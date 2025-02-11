import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_path = '2 bit跳变数量和位置\\times.ttf'  # 字体文件的路径
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'Times New Roman'

data0 = pd.read_table('6.1Algorithms\OptimalOrder\wdelay127wmx.txt', encoding='utf-8', delim_whitespace=True, header=None)
data2 = pd.read_table('6.1Algorithms\OptimalOrder\w127延迟匹配序列.txt', encoding='utf-8', delim_whitespace=True, header=None)
data3 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq1_DelaySeq.txt')
data4 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq2_DelaySeq.txt')
data5 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq3_DelaySeq.txt')
data6 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq4_DelaySeq.txt')
data7 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq5_DelaySeq.txt')
data8 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq6_DelaySeq.txt')
data9 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq7_DelaySeq.txt')
data10 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq8_DelaySeq.txt')
data11 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq9_DelaySeq.txt')

# 绘制小提琴图
# plt.violinplot(data0, showmedians=True)
# plt.violinplot(data2, showmedians=True)
# plt.violinplot(data3, showmedians=True)
# plt.violinplot(data6, showmedians=True)

# 设置绘图样式
fig, axs = plt.subplots(1, 11, figsize=(5, 5))

# 绘制第一个小提琴图
axs[0].violinplot(data0, showmeans=False, showmedians=True)
axs[0].set_title('Data wmx')
axs[0].tick_params(axis='y', labelsize=6)
axs[0].tick_params(axis='x', labelsize=6)
axs[0].set_ylim(2000, 5000)

# 绘制第二个小提琴图
axs[1].violinplot(data2, showmeans=False, showmedians=True)
axs[1].set_title('Data Original')
axs[1].tick_params(axis='y', labelsize=6)
axs[1].tick_params(axis='x', labelsize=6)
axs[1].set_ylim(4500, 5000)

axs[2].violinplot(data3, showmeans=False, showmedians=True)
axs[2].set_title('PE 1')
axs[2].tick_params(axis='y', labelsize=6)
axs[2].tick_params(axis='x', labelsize=6)
axs[2].set_ylim(2000, 5000)

axs[3].violinplot(data4, showmeans=False, showmedians=True)
axs[3].set_title('PE 2')
axs[3].tick_params(axis='y', labelsize=6)
axs[3].tick_params(axis='x', labelsize=6)
axs[3].set_ylim(2000, 5000)
                 
axs[4].violinplot(data5, showmeans=False, showmedians=True)
axs[4].set_title('PE 3')
axs[4].tick_params(axis='y', labelsize=6)
axs[4].tick_params(axis='x', labelsize=6)
axs[4].set_ylim(2000, 5000)

axs[5].violinplot(data6, showmeans=False, showmedians=True)
axs[5].set_title('PE 4')
axs[5].tick_params(axis='y', labelsize=6)
axs[5].tick_params(axis='x', labelsize=6)
axs[5].set_ylim(2000, 5000)

axs[6].violinplot(data7, showmeans=False, showmedians=True)
axs[6].set_title('PE 5')
axs[6].tick_params(axis='y', labelsize=6)
axs[6].tick_params(axis='x', labelsize=6)
axs[6].set_ylim(2000, 5000)

axs[7].violinplot(data8, showmeans=False, showmedians=True)
axs[7].set_title('PE 6')
axs[7].tick_params(axis='y', labelsize=6)
axs[7].tick_params(axis='x', labelsize=6)
axs[7].set_ylim(2000, 5000)

axs[8].violinplot(data9, showmeans=False, showmedians=True)
axs[8].set_title('PE 7')
axs[8].tick_params(axis='y', labelsize=6)
axs[8].tick_params(axis='x', labelsize=6)
axs[8].set_ylim(2000, 5000)

axs[9].violinplot(data10, showmeans=False, showmedians=True)
axs[9].set_title('PE 8')
axs[9].tick_params(axis='y', labelsize=6)
axs[9].tick_params(axis='x', labelsize=6)
axs[9].set_ylim(2000, 5000)

axs[10].violinplot(data11, showmeans=False, showmedians=True)
axs[10].set_title('PE 9')
axs[10].tick_params(axis='y', labelsize=6)
axs[10].tick_params(axis='x', labelsize=6)
axs[10].set_ylim(2000, 5000)



plt.subplots_adjust(wspace=1)

# 设置横轴标签
# plt.xticks(np.arange(1, 10), [f"Sample {i}" for i in range(1, 10)])
#plt.xticks(np.arange(1, 4), [f"PE {i}" for i in range(1, 4)])

# 添加标题和坐标轴标签
# plt.title("Violin Plot")
# plt.xlabel("Samples")
# plt.ylabel("Values")


plt.show()
