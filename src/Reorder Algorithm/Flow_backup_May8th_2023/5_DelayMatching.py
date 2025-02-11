import pandas as pd

# 导入数据
data1 = pd.read_table(r'7.3x3Array\127.txt', encoding='utf-8', delim_whitespace=True, header=None)
data2 = pd.read_table(r'7.3x3Array\3_XORed\seq1_XORed.txt', encoding='utf-8', delim_whitespace=True, header=None)

# 打开输出文件
with open(r'7.3x3Array\4_Delay\seq1_Delay.txt', 'w') as f:
    # 对于序列中的每个数
    for i in range(data2.shape[0]):
        # 在列表中查找对应的输出
        for j in range(data1.shape[0]):
            if data2.iloc[i, 0] == data1.iloc[j, 0]:
                # 将对应的输出写入输出文件
                f.write(str(data1.iloc[j, 1]) + '\n')
                break
