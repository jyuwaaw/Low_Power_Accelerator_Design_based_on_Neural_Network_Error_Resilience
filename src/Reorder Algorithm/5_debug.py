import pandas as pd

for i in range(1, 10):
    # 导入数据
    data1 = pd.read_table(f'255.txt', encoding='utf-8', delim_whitespace=True, header=None)
    data2 = pd.read_table(f'7.3x3Array\\1_initial\\seq{i}_init.txt', encoding='utf-8', delim_whitespace=True, header=None)

    # 打开输出文件
    with open(f'7.3x3Array/5_DelayMatching/i255OG/seq{i}_DelaySeqOG255.txt', 'w') as f:
        # 对于序列中的每个数
        for j in range(data2.shape[0]):
            # 在列表中查找对应的输出
            for k in range(data1.shape[0]):
                if data2.iloc[j, 0] == data1.iloc[k, 0]:
                    # 将对应的输出写入输出文件
                    f.write(str(data1.iloc[k, 1]) + '\n')
                    break
