# 打开索引文件，读取索引数据
with open(r'7.3x3Array\2_IndicesReorder\seq1_zfill_re.txt', 'r') as f:
    index = [int(line.strip()) for line in f]

# 打开原始数据文件，读取数据
with open(r'7.3x3Array\Zfill\seq1_zfill.txt', 'r') as f:
    data = [line.strip() for line in f]

# 根据索引对数据进行重新排序
sorted_data = [data[i] for i in index]

# 将排序结果写入输出文件
with open(r'7.3x3Array\3_Reordered/seq1_reordered.txt', 'w') as f:
    f.write('\n'.join(sorted_data))
