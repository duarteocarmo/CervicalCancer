from numpy import genfromtxt
import pandas as pd
import numpy as np

csv_file_path = '/Users/duarteocarmo/OneDrive - Danmarks Tekniske Universitet/[3rd Semester]/[3rd Semester]02450-Machine Learning/Tools/02450Toolbox_Python/Data/risk_factors_cervical_cancer.csv'

from_file = genfromtxt(csv_file_path, delimiter=',')

from_pandas = pd.read_csv(csv_file_path, header=None)

raw_data_numpy = pd.DataFrame.as_matrix(from_pandas)

header = raw_data_numpy[0, :]

# delete headers from raw data
raw = from_file[1::, :]

# print(raw)
# print(raw, type(raw))

# print headers
# print(header, type(header))






