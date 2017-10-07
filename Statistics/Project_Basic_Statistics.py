from Project_Clean_data import raw
from Project_Clean_data import header
import numpy as np
import xlsxwriter

# We could also define binary headers and only calculate there.


# build statistics function
def __get_basic_stats__(x):
    mean_x = x.mean()
    std_x = x.std(ddof=1)
    median_x = np.median(x)
    range_x = x.max() - x.min()
    norm_x = np.linalg.norm(x)
    min_x = min(x)
    max_x = max(x)
    print('Min:', min_x)
    print('Max:', max_x)
    print('Mean:', mean_x)
    print('Standard Deviation:', std_x)
    print('Median:', median_x)
    print('Range:', range_x)
    print('Norm:', norm_x)


# apply to data
for column_number in range(raw.shape[1]):
    print('Attribute Name: {}'.format(header[column_number]))
    __get_basic_stats__(raw[:, column_number])
    print('\n')


# function that can write to excel file
def __write_basic_stats__(x):
    results = []
    mean_x = x.mean()
    std_x = x.std(ddof=1)
    median_x = np.median(x)
    range_x = x.max() - x.min()
    norm_x = np.linalg.norm(x)
    min_x = min(x)
    max_x = max(x)
    results.append(mean_x)
    results.append(std_x)
    results.append(median_x)
    results.append(range_x)
    results.append(norm_x)
    results.append(min_x)
    results.append(max_x)

    if min_x == 0 and max_x == 1:
        percentage_of_1 = sum(x) * 100.0 / len(x)
        percentage_of_0 = 100.0 - percentage_of_1
        results.append(percentage_of_1)
        results.append(percentage_of_0)

    return results

# Write Everythng to Excel File
workbook = xlsxwriter.Workbook('Statistics.xlsx')
worksheet = workbook.add_worksheet()

row = 1
column = 1

for column_number in range(raw.shape[1]):
    result = __write_basic_stats__(raw[:, column_number])
    for stat in result:
        worksheet.write(row, column, stat)
        column += 1
    column = 1
    row += 1


row = 1
column = 0
for attribute in header:
    worksheet.write(row, column, attribute)
    row += 1


stats = ['Mean', 'Standard Deviation', 'Median', 'Range', 'Norm', 'Minimum', 'Maximum', 'Percentage of 1', 'Percentage of 0']
row = 0
column = 1
for name in stats:
    worksheet.write(row, column, name)
    column += 1

workbook.close()

