'''
with open("weight1w.txt","r") as f:
 sum=0
 f1 = open('w重排序列_org.txt', 'w')
 for line in f:#遍历每一行
     wordlist=line.split()#将每一行的数字分开放在列表中
     for a in wordlist:#遍历每一行的数字
         number=int(a)
         sum=127+number#求和
         x=bin(sum)
         h = (x[2:]).zfill(8)
         f1.write(str(h) + '\n')
f1.close()
f.close()
'''
m1 = 0
with open('Algorithms/OptimalOrder/w127.txt', 'r') as f2:
 f3 = open('Algorithms/OptimalOrder/seqOGw.txt', 'w')
 for line in f2:
    wordlist = line.split()
    
    for b in wordlist:
       #print(wordlist)
        dorg = int(b)
        dquo7 = dorg // 10
        drem7 = dorg % 10
        dquo6 = dquo7 // 10
        drem6 = dquo7 % 10
        dquo5 = dquo6 // 10
        drem5 = dquo6 % 10
        dquo4 = dquo5 // 10
        drem4 = dquo5 % 10
        dquo3 = dquo4 // 10
        drem3 = dquo4 % 10
        dquo2 = dquo3 // 10
        drem2 = dquo3 % 10
        dquo1 = dquo2 // 10
        drem1 = dquo2 % 10    
        dquo0 = dquo1 // 10
        drem0 = dquo1 % 10            
       #quot, rem = divmod(dorg, 10)
    print(drem0,drem1,drem2,drem3,drem4,drem5,drem6,drem7, file = f3)

       

'''
import numpy as np
import pandas as pd
f = open('weight_real1.txt',encoding='utf-8')
f1 = open('weightlist.txt','w',encoding='utf-8')
l = list(f)

cnt = 8
weight = [0' '0' '0' '0' '0' '0' '0' '0]
#weight = np.zeros()


if(cnt > 0)

    rem = a % b


j1 = 0
    while j1 < 8:
    rem = a % b
print (b,file = f1)'''
