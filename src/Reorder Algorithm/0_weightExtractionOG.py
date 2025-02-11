import os

with open(r'7.3x3Array\weights3w_reduced.txt', 'r') as f:
    lines = f.read().split('\n\n')

seqOG = []

for matrix in lines:
    elements = matrix.split(',')
    seqOG.append(str(elements[0]))

with open(r'7.3x3Array/0_weightsExtraction/seqOG.txt', 'w') as f:
    f.write('\n'.join(map(str, seqOG)))