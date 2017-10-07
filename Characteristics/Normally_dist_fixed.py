from matplotlib.pyplot import (figure, hold, subplots, plot, xlabel, ylabel,
                               xticks, yticks,legend, show, title, hist, savefig, close, setp, tight_layout, locator_params)
import numpy as np
# requires data from exercise 4.1.1
from Project_Clean_data import raw
from Project_Clean_data import header
from textwrap import wrap
from scipy import stats

# Keep main attributes and header
important_attributes = [0, 1, 2, 3, 5, 8]
main_raw = raw[:,important_attributes]
main_header = header[important_attributes]

# Compute values of N, M and C.
M = len(important_attributes)
X = main_raw

gen = []
for col in range(M):
    un = []
    for i in range(len(X[:,0])):
        if X[i,col] not in un:
            un.append(X[i,col])
    gen.append(un)

c = 0  
sc = 6  
f, axarr = subplots(3, 2)
for nx in range(3):
    for ny in range(2):
        attribute = X[:,c]
        mean_attribute = attribute.mean()
        std_attribute = attribute.std(ddof=1)
        x = np.linspace(attribute.min(), attribute.max(), 500)
        pdf = stats.norm.pdf(x, loc=mean_attribute, scale=sc)
        axarr[nx,ny].hist(attribute, bins=len(un), normed=True, color='blue')
        axarr[nx,ny].set_title(main_header[c])
        axarr[nx,ny].plot(x, pdf,'.', color='red')
        c += 1
        sc = 1 
tight_layout()
