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
    with open("./b2_output1.csv", "w", encoding="utf-8-sig") as file:
        file.writelines(filtered_table)

table = readCSVFile()
filtered_table = []

for i in range(0, 61):
    table[i] = table[i].split(",")
    if i == 0:
        filtered_table.append(table[i])
    for j in range(0, len(table[i])):
        if j == 11:
            if table[i][j][0:2] == "St":
                filtered_table.append(table[i])

for i in range(0, len(filtered_table)):
    filtered_table[i] = ",".join(filtered_table[i])

writeFile(filtered_table)
        
            

    
    
