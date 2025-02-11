with open('7.3x3Array\weights\seq1.txt','r') as f:
    sum = 0
    f1 = open('7.3x3Array\Zfill\seq1_zfill.txt', 'w')
    for line in f:
        wordlist = line.strip().split()
        for a in wordlist:
            try:
                number = int(a)
            except ValueError:
                print(f"Error: could not convert '{a}' to int in line: {line}")
                continue
            sum = 127 + number
            x = bin(sum)
            h = (x[3:]).zfill(8)
            f1.write(str(h) + '\n')
    f1.close()
