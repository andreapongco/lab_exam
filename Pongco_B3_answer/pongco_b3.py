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
    with open("./b3_output1.csv", "w", encoding="utf-8-sig") as file:
        file.writelines(filtered_table)

table = readCSVFile()
filtered_table = []
unique_table = []
unique_table_dict = {}
for i in range(0, 61):
    table[i] = table[i].split(",")
    for j in range(0, len(table[i])):
        if j == 11:
            filtered_table.append(table[i][j])

for i in filtered_table:
    unique_table_dict[i] = 0

unique_table = list(unique_table_dict.keys())

unique_table[0] = "Scientific Name\n"

for i in range(1, len(unique_table)):
    unique_table[i] = f"{unique_table[i]}\n"

writeFile(unique_table)
        
            

    
    
