import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

for i in range(1, 10):
    filename = f'7.3x3Array\\5_DelayMatching\\seq{i}_DelaySeq.txt'
    data = pd.read_table(filename, header=None, names=['value'])

    x = np.arange(len(data))
    y = data['value']
    s = data.groupby('value').size() ** 2
    
    ax.scatter(x, y, s=s, alpha=0.5, label=f'Group {i}')

ax.legend()
ax.set_xlabel('Index')
ax.set_ylabel('Value')

plt.show()
