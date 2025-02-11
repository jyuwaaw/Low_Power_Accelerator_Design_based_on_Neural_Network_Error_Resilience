'''# 定义9个序列，用于存储所有矩阵的元素
seq1 = []
seq2 = []
seq3 = []
seq4 = []
seq5 = []
seq6 = []
seq7 = []
seq8 = []
seq9 = []

# 逐个读取矩阵
with open("7.3x3Array\weights3w_reduced.txt") as f:
    lines = f.readlines()
    matrix_count = 0
    matrix_lines = []
    for line in lines:
        # 如果读到空行，说明已经读完一个矩阵，需要将其中的元素添加到相应的序列中
        if line.strip() == "":
            for i in range(3):
                row = matrix_lines[i].strip().split(",")
                seq1.append(row[0])
                seq2.append(row[1])
                seq3.append(row[2])
                seq4.append(matrix_lines[0].strip().split(",")[i])
                seq5.append(matrix_lines[1].strip().split(",")[i])
                seq6.append(matrix_lines[2].strip().split(",")[i])
                if i == 0:
                    seq7.append(matrix_lines[i].strip().split(",")[i])
                    seq8.append(matrix_lines[i+1].strip().split(",")[i+1])
                    seq9.append(matrix_lines[i+2].strip().split(",")[i+2])
                elif i == 1:
                    seq7.append(matrix_lines[i-1].strip().split(",")[i])
                    seq8.append(matrix_lines[i].strip().split(",")[i])
                    seq9.append(matrix_lines[i+1].strip().split(",")[i-1])
                else:
                    seq7.append(matrix_lines[i-2].strip().split(",")[i])
                    seq8.append(matrix_lines[i-1].strip().split(",")[i-1])
                    seq9.append(matrix_lines[i].strip().split(",")[i-2])
            # 重置变量以便读取下一个矩阵
            matrix_count += 1
            matrix_lines = []
            if matrix_count == 3:
                break
        else:
            matrix_lines.append(line)

# 将每个序列写到新文件
with open("7.3x3Array\weights\seq1.txt", "w") as f:
    f.write(",".join(seq1))
with open("7.3x3Array\weights\seq2.txt", "w") as f:
    f.write(",".join(seq2))
with open("7.3x3Array\weights\seq3.txt", "w") as f:
    f.write(",".join(seq3))
with open("7.3x3Array\weights\seq4.txt", "w") as f:
    f.write(",".join(seq4))
with open("7.3x3Array\weights\seq5.txt", "w") as f:
    f.write(",".join(seq5))
with open("7.3x3Array\weights\seq6.txt", "w") as f:
    f.write(",".join(seq6))
with open("7.3x3Array\weights\seq7.txt", "w") as f:
    f.write(",".join(seq7))
with open("7.3x3Array\weights\seq8.txt", "w") as f:
    f.write(",".join(seq8))
with open("7.3x3Array\weights\seq9.txt", "w") as f:
    f.write(",".join(seq9))'''


with open('7.3x3Array\weights3w_reduced.txt', 'r') as f:
    lines = f.readlines()

# Initialize empty lists for each sequence
seq1 = []
seq2 = []
seq3 = []
seq4 = []
seq5 = []
seq6 = []
seq7 = []
seq8 = []
seq9 = []

# Loop through each matrix in the input file
for i in range(0, len(lines), 4):
    # Split the lines of the matrix into individual elements
    elements = lines[i].split(',') + lines[i+1].split(',') + lines[i+2].split(',')
    
    # Convert the elements from strings to floats and add them to the appropriate sequences
    seq1.append(str(elements[0]))
    seq2.append(str(elements[1]))
    seq3.append(str(elements[2]))
    seq4.append(str(elements[3]))
    seq5.append(str(elements[4]))
    seq6.append(str(elements[5]))
    seq7.append(str(elements[6]))
    seq8.append(str(elements[7]))
    seq9.append(str(elements[8]))

# Write each sequence to a separate file
with open('7.3x3Array\weights\seq1.txt', 'w') as f:
    f.write('\n'.join(map(str, seq1)))
with open('7.3x3Array\weights\seq2.txt', 'w') as f:
    f.write('\n'.join(map(str, seq2)))
with open('7.3x3Array\weights\seq3.txt', 'w') as f:
    f.write('\n'.join(map(str, seq3)))
with open('7.3x3Array\weights\seq4.txt', 'w') as f:
    f.write('\n'.join(map(str, seq4)))
with open('7.3x3Array\weights\seq5.txt', 'w') as f:
    f.write('\n'.join(map(str, seq5)))
with open('7.3x3Array\weights\seq6.txt', 'w') as f:
    f.write('\n'.join(map(str, seq6)))
with open('7.3x3Array\weights\seq7.txt', 'w') as f:
    f.write('\n'.join(map(str, seq7)))
with open('7.3x3Array\weights\seq8.txt', 'w') as f:
    f.write('\n'.join(map(str, seq8)))
with open('7.3x3Array\weights\seq9.txt', 'w') as f:
    f.write('\n'.join(map(str, seq9)))
