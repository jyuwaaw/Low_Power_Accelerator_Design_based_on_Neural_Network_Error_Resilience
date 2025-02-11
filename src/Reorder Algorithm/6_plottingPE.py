import matplotlib.pyplot as plt

# create figure and axis objects
fig, ax = plt.subplots()

# create gridlines for 3x3 array
for i in range(4):
    ax.axhline(y=i, color='black', linewidth=1)
    ax.axvline(x=i, color='black', linewidth=1)

# create labels for each PE
pe_labels = ['PE0', 'PE1', 'PE2', 'PE3', 'PE4', 'PE5', 'PE6', 'PE7', 'PE8']

# add labels to PEs
for i in range(9):
    ax.text(i%3 + 0.2, i//3 + 0.5, pe_labels[i], fontsize=14)

# remove ticks from axis
ax.set_xticks([])
ax.set_yticks([])

# show plot
plt.show()
