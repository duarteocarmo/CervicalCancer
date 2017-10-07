import numpy as np
from Project_Clean_data import raw
from Project_Clean_data import header
from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show, legend, hold, subplot, xticks, yticks
from scipy.linalg import svd
import matplotlib.pyplot as plt


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


# Project the centered data onto principal component space
Z = np.dot(Y, V)
# Z = Y * V




# Number of PCAS to plot
k = 4

print(V.shape)
print(len(header))
print(V[:,1].T)
for i in range(k):
    plt.plot(range(len(V[:, i])), V[:, i], '--')
    print('The min of PCA{} corresponds to the attribute {}'.format(i + 1, header[np.argmin(V[:, i])]))
    print('The max of PCA{} corresponds to the attribute {}'.format(i + 1, header[np.argmax(V[:, i])]))
plt.title('Amount of Variation per Principal Component')
legend(['PCA1', 'PCA2', 'PCA3', 'PCA4'])
xlabel('Attributes')
ylabel('Amount of variation')
plt.show()





