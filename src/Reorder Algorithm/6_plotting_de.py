import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#file0 = open('w127延迟匹配序列.txt')
#file1 = open('w异或延迟匹配序列.txt')
data0 = pd.read_table('6.1Algorithms\OptimalOrder\wdelay127wmx.txt', encoding='utf-8', delim_whitespace=True, header=None)
#data1 = pd.read_table('6.1Algorithms\OptimalOrder\w127OO_DelayMatching_1.txt', encoding='utf-8', delim_whitespace=True, header=None)
data2 = pd.read_table('6.1Algorithms\OptimalOrder\w127延迟匹配序列.txt', encoding='utf-8', delim_whitespace=True, header=None)
data3 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq1_DelaySeq.txt') # Delay of Seq1
data4 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq2_DelaySeq.txt')
data5 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq3_DelaySeq.txt')
data6 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq4_DelaySeq.txt')
data7 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq5_DelaySeq.txt')
data8 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq6_DelaySeq.txt')
data9 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq7_DelaySeq.txt')
data10 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq8_DelaySeq.txt')
data11 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq9_DelaySeq.txt')



#data0 = pd.read_table('w127延迟匹配序列.txt', encoding='utf-8', delim_whitespace=True, header=None)
#data1 = pd.read_table('w127延迟匹配序列org.txt', encoding='utf-8', delim_whitespace=True, header=None)

plt.figure()
plt.title('input=127')
#plt.plot(para0_0,para0_1,para1_0,para1_1)
# plt.plot(data0,linewidth =2.0,color='blue')
# plt.plot(data1,linewidth =2.0,color='red')
# plt.plot(data2,linewidth =2.0,color='purple')
# # plt.plot(data3,linewidth =2.0,color='black')
plt.plot(data0, linewidth=2.0, linestyle=':', color=(0.063, 0.275, 0.502), label='wmx')
# plt.plot(data1, linewidth=2.0, linestyle='--', color=(0.427, 0.678, 0.820), label='QuickSort')

plt.plot(data2, linewidth=2.0, linestyle=':', color='#FF5733', label='OriginalDelay')
plt.plot(data3, linewidth=2.0, linestyle=':', color='#00FF00', label='PE[0,0]')
plt.plot(data4, linewidth=2.0, linestyle=':', color='#00BFFF', label='PE[0,1]')
plt.plot(data5, linewidth=2.0, linestyle=':', color='#800080', label='PE[0,2]')
plt.plot(data6, linewidth=2.0, linestyle=':', color='#FFD700', label='PE[1,0]')
plt.plot(data7, linewidth=2.0, linestyle=':', color='#FF00FF', label='PE[1,1]')
plt.plot(data8, linewidth=2.0, linestyle=':', color='#00CED1', label='PE[1,2]')
plt.plot(data9, linewidth=2.0, linestyle=':', color='#FF4500', label='PE[2,0]')
plt.plot(data10, linewidth=2.0, linestyle=':', color='#DC143C', label='PE[2,1]')
plt.plot(data11, linewidth=2.0, linestyle=':', color='#FF1493', label='PE[2,2]')

# plt.boxplot(data2,  color='#FF5733', label='OriginalDelay')
# plt.boxplot(data4,  color='#00BFFF', label='PE[0,1]')
# plt.boxplot(data5,  color='#800080', label='PE[0,2]')
# plt.boxplot(data6,  color='#FFD700', label='PE[1,0]')
# plt.boxplot(data7,  color='#FF00FF', label='PE[1,1]')
# plt.boxplot(data8,  color='#00CED1', label='PE[1,2]')
# plt.boxplot(data9,  color='#FF4500', label='PE[2,0]')
# plt.boxplot(data10,  color='#DC143C', label='PE[2,1]')
# plt.boxplot(data11,  color='#FF1493', label='PE[2,2]')

plt.legend()



plt.ylim(0,6000)
plt.xlim(0,120)

plt.show()