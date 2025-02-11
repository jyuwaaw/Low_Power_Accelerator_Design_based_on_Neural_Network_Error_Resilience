for i in range(1, 10):
    # 输入文件名
    input_file = f"7.3x3Array/weights/seq{i}.txt"
    # 输出文件名
    output_file = f"7.3x3Array/Zfill/seq{i}_zfill.txt"

    with open(input_file, 'r') as f:
        with open(output_file, 'w') as f1:
            sum = 0
            for line in f:
                wordlist = line.strip().split()
                for a in wordlist:
                    try:
                        number = int(a)
                    except ValueError:
                        #print(f"Error: could not convert '{a}' to int in line: {line}")
                        continue
                    sum = 127 + number
                    x = bin(sum)
                    h = (x[3:]).zfill(8)
                    f1.write(str(h) + '\n')
