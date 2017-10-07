from matplotlib.pyplot import (figure, hold, subplot, plot, xlabel, ylabel,
                               xticks, yticks,legend,show)
import numpy as np
# requires data from exercise 4.1.1
from Project_Clean_data import raw
from Project_Clean_data import header
from textwrap import wrap
import matplotlib.pyplot as plt

from scipy import stats




# Keep main attributes and header
important_attributes = [0, 1, 2, 3, 5, 8, 11]
main_raw = raw[:,important_attributes]
main_header = header[important_attributes]
main_header = [ '\n'.join(wrap(l, 20)) for l in main_header ]


# Compute values of N, M and C.
M = len(important_attributes)
X = main_raw

# Prepare the normal distributions
mu = X.mean(axis=0)
s = X.std(ddof=1, axis=0)
S = np.cov(X, rowvar=0, ddof=1)
ngen = X.shape[0]
Xmvgen = np.random.multivariate_normal(mu, S, ngen)

for column in range(M-(M-1)):
    # attribute vector, means and stdv
    attribute = X[:, column]
    mean_attribute = attribute.mean()
    std_attribute = attribute.std(ddof=1)

    # plot the histogram of the normal distribution
    normal = np.random.normal(mean_attribute, std_attribute, X.shape[0])
    plt.hist(normal)
    plt.hist(attribute)

    # plot the probability density curve
    # NOT WORKING!!!!!!!!!!
    x = np.linspace(attribute.min(), attribute.max(), len(attribute))
    pdf = stats.norm.pdf(x, loc=mean_attribute, scale=0.2)
    plt.plot(x, pdf, '.', color='red')





    plt.show()



