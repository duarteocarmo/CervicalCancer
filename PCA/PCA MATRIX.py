import numpy as np
from Project_Clean_data import raw
from Project_Clean_data import header
from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show, legend, hold, subplot, xticks, yticks
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


# Number of PCAS to plot
k = 4

figure(figsize=(12,10))
hold(True)
for i in range(k):
    for j in range(k):
        subplot(k, k, i*k + j + 1)
        for c in range(C):
            class_mask = (y == c)
            plot(Z[class_mask, i], Z[class_mask, j], '.')
            if i==k-1:
                xlabel('PCA{}'.format(j+1), fontsize=10)
            else:
                xticks([])
            if j==0:
                ylabel('PCA{}'.format(i+1), fontsize=10)
            else:
                yticks([])
            #ylim(0,X.max()*1.1)
            #xlim(0,X.max()*1.1)

legend(classNames)

show()














