from Project_Import_data import raw
from Project_Import_data import header
import numpy as np
import math
import random
import pandas as pd


since_first = header[26]
since_last = header[27]

raw = np.delete(raw, [26, 27], 1)
header = np.delete(header, [26, 27])

integer = [0, 1, 2, 3]


Dx = list(header).index('Dx')


def is_binary(x):
    if min(x) == 0 and max(x) == 1:
        return True
    else:
        return False

meanlst = []
for i in range(len(raw[0])):
    lst = []
    for n in range(len(raw)):
        if math.isnan(raw[n,i]) is False:
            lst.append(raw[n,i])
    mean = sum(lst)/len(lst)
    meanlst.append(mean)


for i in range(raw.shape[0]):
    for j in range(raw.shape[1]):

        if math.isnan(raw[i, j]) is True and is_binary(raw[:, j]) is False:
            if j not in integer:
                raw[i, j] = meanlst[j]
            else:
                raw[i, j] = round(meanlst[j])

        if math.isnan(raw[i, j]) is True and is_binary(raw[:, j]) is True:
            number_of_zeros = np.count_nonzero(raw[:, j] == 0)
            number_of_ones = np.count_nonzero(raw[:, j] == 1)
            percentage_0 = number_of_zeros / (number_of_zeros + number_of_ones)
            raw[i, j] = np.random.choice(([0, 1]), p=[percentage_0, 1 - percentage_0])


nan_counter = 0

for i in range(raw.shape[0]):
    for j in range(raw.shape[1]):
        if math.isnan(raw[i, j]) is True:
            print('We got a nan')

exwrite = pd.DataFrame(raw)
exwrite.to_excel('data.xlsx', header=header)
