import os

with open(r'7.3x3Array\weights3w_reduced.txt', 'r') as f:
    lines = f.read().split('\n\n')

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
for matrix in lines:
    # Split the lines of the matrix into individual elements
    elements = matrix.split(',')
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
with open(r'7.3x3Array/0_weightsExtraction/seq1.txt', 'w') as f:
    f.write('\n'.join(map(str, seq1)))
with open(r'7.3x3Array/0_weightsExtraction/seq2.txt', 'w') as f:
    f.write('\n'.join(map(str, seq2)))
with open(r'7.3x3Array/0_weightsExtraction/seq3.txt', 'w') as f:
    f.write('\n'.join(map(str, seq3)))
with open(r'7.3x3Array/0_weightsExtraction/seq4.txt', 'w') as f:
    f.write(''.join(map(str, seq4)))
with open(r'7.3x3Array/0_weightsExtraction/seq5.txt', 'w') as f:
    f.write('\n'.join(map(str, seq5)))
with open(r'7.3x3Array/0_weightsExtraction/seq6.txt', 'w') as f:
    f.write('\n'.join(map(str, seq6)))
with open(r'7.3x3Array/0_weightsExtraction/seq7.txt', 'w') as f:
    f.write(''.join(map(str, seq7)))
with open(r'7.3x3Array/0_weightsExtraction/seq8.txt', 'w') as f:
    f.write('\n'.join(map(str, seq8)))
with open(r'7.3x3Array/0_weightsExtraction/seq9.txt', 'w') as f:
    f.write('\n'.join(map(str, seq9)))
