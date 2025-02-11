import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_path = '2 bit跳变数量和位置\\times.ttf'  # 字体文件的路径
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'Times New Roman'

# # data0 = pd.read_table('6.1Algorithms\OptimalOrder\wdelay127wmx.txt', encoding='utf-8', delim_whitespace=True, header=None)
# data2 = pd.read_table('6.1Algorithms\OptimalOrder\w127延迟匹配序列.txt', encoding='utf-8', delim_whitespace=True, header=None)
data0 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255OG\seq1_DelaySeqOG255.txt')
data1 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255OG\seq2_DelaySeqOG255.txt')
data2 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255OG\seq3_DelaySeqOG255.txt')
data3 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255OG\seq4_DelaySeqOG255.txt')
data4 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255OG\seq5_DelaySeqOG255.txt')
data5 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255OG\seq6_DelaySeqOG255.txt')
data6 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255OG\seq7_DelaySeqOG255.txt')
data7 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255OG\seq8_DelaySeqOG255.txt')
data8 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255OG\seq9_DelaySeqOG255.txt')

data9 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255\seq1_DelaySeq255.txt')
data10 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255\seq2_DelaySeq255.txt')
data11 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255\seq3_DelaySeq255.txt')
data12 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255\seq4_DelaySeq255.txt')
data13 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255\seq5_DelaySeq255.txt')
data14 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255\seq6_DelaySeq255.txt')
data15 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255\seq7_DelaySeq255.txt')
data16 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255\seq8_DelaySeq255.txt')
data17 = pd.read_table(r'7.3x3Array\5_DelayMatching\i255\seq9_DelaySeq255.txt')

# 设置绘图样式
fig, axs = plt.subplots(2, 9, figsize=(16, 8))

axs = axs.flatten()

axs[0].violinplot(data0, showmeans=False, showmedians=True)
axs[0].set_title('PE 1')
axs[0].tick_params(axis='y', labelsize=6)
axs[0].tick_params(axis='x', labelsize=6)
axs[0].set_ylim(1000, 5000)

axs[1].violinplot(data1, showmeans=False, showmedians=True)
axs[1].set_title('PE 2')
axs[1].tick_params(axis='y', labelsize=6)
axs[1].tick_params(axis='x', labelsize=6)
axs[1].set_ylim(1000, 5000)

axs[2].violinplot(data2, showmeans=False, showmedians=True)
axs[2].set_title('PE 3')
axs[2].tick_params(axis='y', labelsize=6)
axs[2].tick_params(axis='x', labelsize=6)
axs[2].set_ylim(1000, 5000)

axs[3].violinplot(data3, showmeans=False, showmedians=True)
axs[3].set_title('PE 4')
axs[3].tick_params(axis='y', labelsize=6)
axs[3].tick_params(axis='x', labelsize=6)
axs[3].set_ylim(1000, 5000)

axs[4].violinplot(data4, showmeans=False, showmedians=True)
axs[4].set_title('PE 5')
axs[4].tick_params(axis='y', labelsize=6)
axs[4].tick_params(axis='x', labelsize=6)
axs[4].set_ylim(1000, 5000)
                 
axs[5].violinplot(data5, showmeans=False, showmedians=True)
axs[5].set_title('PE 6')
axs[5].tick_params(axis='y', labelsize=6)
axs[5].tick_params(axis='x', labelsize=6)
axs[5].set_ylim(1000, 5000)

axs[6].violinplot(data6, showmeans=False, showmedians=True)
axs[6].set_title('PE 7')
axs[6].tick_params(axis='y', labelsize=6)
axs[6].tick_params(axis='x', labelsize=6)
axs[6].set_ylim(1000, 5000)

axs[7].violinplot(data7, showmeans=False, showmedians=True)
axs[7].set_title('PE 8')
axs[7].tick_params(axis='y', labelsize=6)
axs[7].tick_params(axis='x', labelsize=6)
axs[7].set_ylim(1000, 5000)

axs[8].violinplot(data8, showmeans=False, showmedians=True)
axs[8].set_title('PE 9')
axs[8].tick_params(axis='y', labelsize=6)
axs[8].tick_params(axis='x', labelsize=6)
axs[8].set_ylim(1000, 5000)

axs[9].violinplot(data9, showmeans=False, showmedians=True)
axs[9].set_title('PE 1')
axs[9].tick_params(axis='y', labelsize=6)
axs[9].tick_params(axis='x', labelsize=6)
axs[9].set_ylim(1000, 5000)

axs[10].violinplot(data10, showmeans=False, showmedians=True)
axs[10].set_title('PE 2')
axs[10].tick_params(axis='y', labelsize=6)
axs[10].tick_params(axis='x', labelsize=6)
axs[10].set_ylim(1000, 5000)

axs[11].violinplot(data11, showmeans=False, showmedians=True)
axs[11].set_title('PE 3')
axs[11].tick_params(axis='y', labelsize=6)
axs[11].tick_params(axis='x', labelsize=6)
axs[11].set_ylim(1000, 5000)


axs[12].violinplot(data11, showmeans=False, showmedians=True)
axs[12].set_title('PE 4')
axs[12].tick_params(axis='y', labelsize=6)
axs[12].tick_params(axis='x', labelsize=6)
axs[12].set_ylim(1000, 5000)


axs[13].violinplot(data11, showmeans=False, showmedians=True)
axs[13].set_title('PE 5')
axs[13].tick_params(axis='y', labelsize=6)
axs[13].tick_params(axis='x', labelsize=6)
axs[13].set_ylim(1000, 5000)


axs[14].violinplot(data11, showmeans=False, showmedians=True)
axs[14].set_title('PE 6')
axs[14].tick_params(axis='y', labelsize=6)
axs[14].tick_params(axis='x', labelsize=6)
axs[14].set_ylim(1000, 5000)


axs[15].violinplot(data11, showmeans=False, showmedians=True)
axs[15].set_title('PE 7')
axs[15].tick_params(axis='y', labelsize=6)
axs[15].tick_params(axis='x', labelsize=6)
axs[15].set_ylim(1000, 5000)


axs[16].violinplot(data11, showmeans=False, showmedians=True)
axs[16].set_title('PE 8')
axs[16].tick_params(axis='y', labelsize=6)
axs[16].tick_params(axis='x', labelsize=6)
axs[16].set_ylim(1000, 5000)


axs[17].violinplot(data11, showmeans=False, showmedians=True)
axs[17].set_title('PE 9')
axs[17].tick_params(axis='y', labelsize=6)
axs[17].tick_params(axis='x', labelsize=6)
axs[17].set_ylim(1000, 5000)




plt.subplots_adjust(wspace=1)

# 设置横轴标签
# plt.xticks(np.arange(1, 10), [f"Sample {i}" for i in range(1, 10)])
#plt.xticks(np.arange(1, 4), [f"PE {i}" for i in range(1, 4)])

# 添加标题和坐标轴标签
# plt.title("Violin Plot")
# plt.xlabel("Samples")
# plt.ylabel("Values")


plt.show()
