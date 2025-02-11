from os import path

def process_file(seq_num: int):
    # 读取输入文件中的原始序列
    with open(path.join( f'7.3x3Array/3_weightReorder/seq{seq_num}_wReordered.txt'), 'r') as f:
        seq = [int(line.strip(), 2) for line in f]

    # 计算相邻两个数的异或结果
    xor_seq = []
    for i in range(len(seq)-1):
        xor_result = seq[i] ^ seq[i+1]
        xor_seq.append(xor_result)

    # 将结果写入输出文件
    with open(path.join( f'7.3x3Array/4_XOR/seq{seq_num}_XORed.txt'), 'w') as f:
        for xor_result in xor_seq:
            f.write(bin(xor_result)[2:].zfill(8) + '\n')


# 处理9个输入文件
for i in range(1, 10):
    process_file(i)
