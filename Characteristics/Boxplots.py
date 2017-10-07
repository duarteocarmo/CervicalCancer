from Project_Clean_data import raw
from Project_Clean_data import header
from matplotlib.pyplot import boxplot, xticks, ylabel, title, show
import numpy as np
from textwrap import wrap


# find integer columns
integer = []
for column in range(raw.shape[1]):
    if np.array_equal(raw[:, column], raw[:, column].astype(bool)) is True:
        continue
    else:
        integer.append(column)


# data and header with only integer attributes
raw_nobinary = raw[:, integer]
header_nobinary = header[integer]


# outlier detection
for column in range(raw_nobinary.shape[1]):
    number_of_outliers = 0
    vector = raw_nobinary[:, column]
    minimum = np.amin(vector)
    maximum = np.amax(vector)
    q50 = np.percentile(vector, 50)
    q75 = np.percentile(vector, 75)
    q25 = np.percentile(vector, 25)
    upper = min(maximum, q75 + 1.5 * (q75 - q25))
    lower = max(minimum, q25 - 1.5 * (q75 - q25))

    for row in range(raw_nobinary.shape[0]):
        if raw_nobinary[row, column] > upper or raw_nobinary[row, column] < lower:
            number_of_outliers += 1

    print(header_nobinary[column], round(number_of_outliers * 100 / np.size(vector)), '% are outliers.')




# Wrap labels
labels = [ '\n'.join(wrap(l, 20)) for l in header_nobinary ]

# Box plot the data
boxplot(raw_nobinary, 0, 'r.')
xticks(range(1,np.size(header_nobinary)+1),labels,rotation=45, fontsize=6)
title('Cervical Cancer Analysis - Attributes')
show()



