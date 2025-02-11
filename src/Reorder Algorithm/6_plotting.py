import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#file0 = open('w127延迟匹配序列.txt')
#file1 = open('w异或延迟匹配序列.txt')
# data0 = pd.read_table('6.1Algorithms\OptimalOrder\wdelay127wmx.txt', encoding='utf-8', delim_whitespace=True, header=None)
# data1 = pd.read_table('6.1Algorithms\OptimalOrder\w127OO_DelayMatching_1.txt', encoding='utf-8', delim_whitespace=True, header=None)
data2 = pd.read_table(r'7.3x3Array\5_DelayMatching\og_DelaySeq.txt')
data3 = pd.read_table(r'7.3x3Array\5_DelayMatching\OG\seq1_DelaySeq.txt')

#data0 = pd.read_table('w127延迟匹配序列.txt', encoding='utf-8', delim_whitespace=True, header=None)
#data1 = pd.read_table('w127延迟匹配序列org.txt', encoding='utf-8', delim_whitespace=True, header=None)

plt.figure()
plt.title('input=127')
#plt.plot(para0_0,para0_1,para1_0,para1_1)
# plt.plot(data0,linewidth =2.0,color='blue')
# plt.plot(data1,linewidth =2.0,color='red')
# plt.plot(data2,linewidth =2.0,color='purple')
# plt.plot(data3,linewidth =2.0,color='black')
# plt.plot(data0, linewidth=2.0, linestyle=':', color=(0.063, 0.275, 0.502), label='wmx')
# plt.plot(data1, linewidth=2.0, linestyle='--', color=(0.427, 0.678, 0.820), label='QuickSort')
plt.plot(data2, linewidth=2.0, linestyle='-.', color='blue', label='Original Delay')
plt.plot(data3, linewidth=2.0, linestyle='-', color=(0.718, 0.133, 0.188), label='Reordered Delay')
plt.legend()



plt.ylim(0,6000)

plt.show()