import numpy as np
from Project_Clean_data import raw
from Project_Clean_data import header
from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show, legend
from scipy.linalg import svd


classDict = {'Negative': 0, 'Positive': 1 }
classNames = classDict.keys()
Dx = list(header).index('Dx')
y = raw[:, Dx]
C = len(classNames)


raw = np.delete(raw,list(header).index('Dx'), 1)
header = np.delete(header,list(header).index('Dx'), 0)



X = raw

N = raw.shape[0]

# Subtract mean value from data
Y = (X - np.ones((N,1))*X.mean(0))


# PCA by computing SVD of Y
U,S,V = svd(Y,full_matrices=False)

V = V.T

print(V.shape)
# Project the centered data onto principal component space
Z = np.dot(Y, V)
# Z = Y * V

print(Z.shape)


# Indices of the principal components to be plotted
i = 0
j = 1

# Plot PCA of the data
f = figure()
f.hold()
title('CC Risk Factors Data: PCA')
#Z = array(Z)
for c in range(C):
    # select indices belonging to class c:
    class_mask = (c == y)
    plot(Z[class_mask,i], Z[class_mask,j], '.')
legend(classNames)
xlabel('PC{0}'.format(i+1))
ylabel('PC{0}'.format(j+1))

# Output result to screen
show()