import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_path = '2 bit跳变数量和位置\\times.ttf'  # 字体文件的路径
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'Times New Roman'


# 读取9个数据表，存储到data列表中
data = []
for i in range(1, 10):
    filename = f'7.3x3Array\\5_DelayMatching\\i255\\seq{i}_DelaySeq255.txt'
    df = pd.read_table(filename, header=None, names=['value'])
    data.append(df)

dataOG = []
for i in range(1, 10):
    filename = f'7.3x3Array\\5_DelayMatching\\i255OG\\seq{i}_DelaySeqOG255.txt'
    df = pd.read_table(filename, header=None, names=['value'])
    dataOG.append(df)

# cmp_data_wmx = pd.read_table('6.1Algorithms\OptimalOrder\wdelay127wmx.txt', header=None, names=['value'])
# cmp_data_og = pd.read_table(r'7.3x3Array\\5_DelayMatching\i255\seqOG_DelaySeq255.txt', header=None, names=['value'])

# 绘制散点图
fig, axs = plt.subplots(6, 3)
axs = axs.ravel()

markers = ['o', 's', 'D', 'p', 'v', '*', 'X', 'd', '^']  # 不同形状

# PE阵列的绘图


for i, df in enumerate(dataOG):
    x = range(1, len(df)+1)
    y = df['value']
    axs[i+9].scatter(x, y, marker='o', color='skyblue', s = 3)
    axs[i+9].set_title(f'PE {i+1}')
    # axs[i+9].set_xlabel('Data Original')
    # axs[i+9].set_ylabel('Delay Value')
    axs[i+9].set_ylim(1000, 6000)
    axs[i+9].set_xlim(0, 400)


for i, df in enumerate(data):
    x = range(1, len(df)+1)
    y = df['value']
    axs[i].scatter(x, y, marker='o', color='#FF4500', s = 3)
    axs[i].set_title(f'PE {i+1}')
    # axs[i].set_xlabel('Data')
    # axs[i].set_ylabel('Delay Value')
    axs[i].set_ylim(1000, 6000)
    axs[i].set_xlim(0, 400)


# # 绘制所有数据的汇总图
# for i, df in enumerate(data):
#     x = range(1, len(df)+1)
#     y = df['value']
#     axs[10].scatter(x, y, marker='o', color='#FF4500',s=3)
#     axs[10].set_xlabel('3x3 PE array')
#     axs[10].set_ylabel('Delay Value')
#     axs[10].set_ylim(1000, 6000)
#     axs[10].set_xlim(0, 400)
# axs.legend()
# axs.set_title('Delay value scatter plot of a 3x3 PE array')
# axs.set_xlabel('Data index')
# axs.set_ylabel('Delay value')
# axs.set_ylim(1000, 6000)

#对比数据的绘图
# x = range(1, len(cmp_data_wmx)+1)
# y = cmp_data_wmx['value']
# axs[i+1].scatter(x, y, marker='o', color='green', s = 5)
# axs[i+1].set_title('wmx')
# axs[i+1].set_xlabel('Data')
# axs[i+1].set_ylabel('Delay Value')
# axs[i+1].set_ylim([1000, 6000])  # 设置y轴范围

# x = range(1, len(cmp_data_og)+1)
# y = cmp_data_og['value']
# axs[i+3].scatter(x, y, marker='o', color='skyblue', s = 5)
# axs[i+3].set_title('Original')
# axs[i+3].set_xlabel('Data')
# axs[i+3].set_ylabel('Delay Value')
# axs[i+3].set_ylim([1000, 6000])  # 设置y轴范围
# axs[i+3].set_xlim(0, 400)



# 设置图例、标题、坐标轴标签等
fig.legend()
fig.suptitle('Input = 255')
fig.text(0.5, 0.04, 'Data index', ha='center')
fig.text(0.04, 0.5, 'Delay value', va='center', rotation='vertical')

plt.subplots_adjust(wspace=0.4,hspace=0.6)

# plt.tight_layout()
plt.show()
