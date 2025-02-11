import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd

font_path = '2 bit跳变数量和位置\\times.ttf'  # 字体文件的路径
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'Times New Roman'

# 从第一个.txt文件读取数据
with open(r'7.3x3Array\5_DelayMatching\seq1_DelaySeq.txt') as file1:
    data1 = [float(line.strip()) for line in file1.readlines()]

# 从第二个.txt文件读取数据
with open(r'7.3x3Array\5_DelayMatching\seq1_DelaySeq_anb.txt') as file2:
    data2 = [float(line.strip()) for line in file2.readlines()]

# 确定x轴数据为索引值
x1 = range(len(data1))
x2 = range(len(data2))

# 创建图形对象
fig, ax = plt.subplots()

# 绘制第一组数据的散点图
ax.scatter(x1, data1, color='skyblue', s = 8, label='Previous Sequence')

# 绘制第二组数据的散点图
ax.scatter(x2, data2, color='#FF4500', s = 8, label='Current Sequence with More Data')

# 设置图形标题和轴标签
ax.set_title('Delay Value of Input Sequence')
ax.set_xlabel('Data')
ax.set_ylabel('Delay Value')
ax.set_xlim([0,400])
ax.set_ylim([1000,6000])

# 显示图例
ax.legend()

# 显示图形
plt.show()

