"""
Author: Andrea Kristine S. Pongco
Date of Development: December 4, 2023
Course: CMSC 191/BIO 191 (Laboratory Exam)
"""

import pandas as pd
import csv
import re

def readCSVFile():
    with open("../Exam_Table.csv", "r", encoding="utf-8-sig") as file:
        words = file.readlines()
        return words

def writeFile(filtered_table):
    with open("./b4_output1.csv", "w", encoding="utf-8-sig") as file:
        file.writelines(filtered_table)

table = readCSVFile()
estimated_sizes = {}

for i in range(0, 61):
    table[i] = table[i].split(",")
    if i != 0:
        table[i] = [table[i][-3], int(table[i][-1][0:-1])]

for i in range(1, 61):
    if table[i][0] not in estimated_sizes.keys():
        estimated_sizes[table[i][0]] = [table[i][1]]
    else:
        estimated_sizes[table[i][0]].append(table[i][1])

write_in_file = [f"{table[0][-3]},Average Est Size\n"]

for i in estimated_sizes:
    summation = 0
    for j in range(0, len(estimated_sizes[i])):
        summation += estimated_sizes[i][j]
    estimated_sizes[i] = summation/len(estimated_sizes[i])
    write_in_file.append(f"{i},{estimated_sizes[i]}\n")

writeFile(write_in_file)


        
            

    
    
