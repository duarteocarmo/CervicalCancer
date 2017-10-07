import numpy as np
from Project_Clean_data import raw
from Project_Clean_data import header
from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show
from scipy.linalg import svd

raw = np.delete(raw,list(header).index('Dx'), 1)

X = raw

N = raw.shape[0]

# Subtract mean value from data
Y = (X - np.ones((N,1))*X.mean(0))


# PCA by computing SVD of Y
U,S,V = svd(Y,full_matrices=False)

# Compute variance explained by principal components
rho = (S*S) / (S*S).sum()

# Amounts of Variation
variation = range(1,len(rho)+1)
count = 0
amount = 0
for variation in rho:
    count += 1
    amount = amount + variation
    print('With {} components, {} percent of the variation is accounted for.'.format(count, round(amount * 100)))

# Plot variance explained
figure()
plot(range(1,len(rho)+1),rho,'o-')
title('Variance explained by principal components');
xlabel('Principal component');
ylabel('Variance explained');
show()





