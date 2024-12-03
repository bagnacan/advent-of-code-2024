# Day 1:
# Given an input file that contains numerical values in two columns separated by
# a triple space, sort each column and sum the distance among each value pair

import csv

delimiter = '   '  # column delimiter
column1 = []
column2 = []
columnd = 0  # difference among column values

# read each column from the input file
with open('data/day_01/input', mode='r') as file:
    for line in file:
        columns = line.split(delimiter)

        column1.append(int(columns[0]))
        column2.append(int(columns[1]))

# sort each column
column1.sort()
column2.sort()

# sum distance among column values
for item in range(len(column1)):
    columnd += abs(column2[item] - column1[item])

print(columnd)

