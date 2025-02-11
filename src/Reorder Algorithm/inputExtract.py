import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # None处也可以是想要的具体数值
#显示所有行
pd.set_option('display.max_rows', None)
#显示宽度无限长
pd.set_option('display.width', None)


all = 256
cnt = 0
n = 128

#f = open('127.txt','w')
f = open('128.txt','w')
f1 = open(r'win.txt', encoding='utf-8')
while cnt < all:
    data1 = pd.read_table('win.txt', encoding='utf-8', delim_whitespace=True, header=None)
    print(data1.iloc[n,0], data1.iloc[n,2], file = f)
    if(data1.iloc[n,2] == 128):
        f.write(str(data1.iloc[n,]) + '\n')
        
        
    cnt = cnt + 1
    n = n + 255
    #print(str(data1.iloc[n,0]) + ' ' + str(data1.iloc[n,1]) + ' ' + str(data1.iloc[n,2]) +'\n', file = f)


