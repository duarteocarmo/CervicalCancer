from matplotlib.pyplot import (figure, hold, subplot, plot, xlabel, ylabel,
                               xticks, yticks,legend,show)
import numpy as np
# requires data from exercise 4.1.1
from Project_Clean_data import raw
from Project_Clean_data import header
from textwrap import wrap


classDict = {'Negative': 0, 'Positive': 1 }
classNames = classDict.keys()
Dx = list(header).index('Dx')
y = raw[:, Dx]
C = len(classNames)
print(sum(y))
print(len(y))
print(y)



# Keep main attributes and header
important_attributes = [0, 1, 2, 3, 5, 8, 11]
main_raw = raw[:,important_attributes]
main_header = header[important_attributes]


main_header = [ '\n'.join(wrap(l, 20)) for l in main_header ]


# Compute values of N, M and C.
M = len(important_attributes)
X = main_raw

figure(figsize=(12,10))
hold(True)
for m1 in range(M):
    for m2 in range(M):
        subplot(M, M, m1*M + m2 + 1)
        for c in range(C):
            class_mask = (y == c)
            plot(np.array(X[class_mask, m2]), np.array(X[class_mask, m1]), '.')
            if m1==M-1:
                xlabel(main_header[m2], fontsize=7)
            else:
                xticks([])
            if m2==0:
                ylabel(main_header[m1], fontsize=7)
            else:
                yticks([])
            #ylim(0,X.max()*1.1)
            #xlim(0,X.max()*1.1)

legend(classNames)

show()




