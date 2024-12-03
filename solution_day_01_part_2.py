# Day 1:
# Given an input file that contains numerical values in two columns separated by
# a triple space, count the number of times a value from the left (column1)
# column appears in the right (column2) column, then multiply that value by the
# count. Repeat this for each value in the left column and sum each result in a
# variable "similarity score"

import csv

delimiter = '   '  # column delimiter
column1 = []
column2 = []
cache = {}
sim_score = 0  # similarity score among column values

# read each column from the input file
with open('data/day_01/input', mode='r') as file:
    for line in file:
        columns = line.split(delimiter)

        column1.append(int(columns[0]))
        column2.append(int(columns[1]))

# sort the lookup column
column2.sort()

# cache values from column1 that we already looked up in column2
for item in column1:

    # lookup new items, or rely on the cache
    occurrences = cache.get(item, None)
    if not occurrences:  # item not cached
        occurrences = column2.count(item)
        cache[item] = occurrences
    sim_score += (item * occurrences)

print(sim_score)

