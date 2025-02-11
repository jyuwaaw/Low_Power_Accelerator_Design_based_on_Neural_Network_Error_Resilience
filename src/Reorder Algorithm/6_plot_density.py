import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data6 = pd.read_table(r'7.3x3Array\5_DelayMatching\seq4_DelaySeq.txt')

plt.hist(data6, bins=30, density=True, alpha=0.5, color='blue')
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Density Plot')

# 显示图形
plt.show()