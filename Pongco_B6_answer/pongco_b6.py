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
    with open("./b6_output1.csv", "w", encoding="utf-8-sig") as file:
        file.writelines(filtered_table)

table = readCSVFile()

for i in range(0, 61):
    table[i] = table[i].split(",")
    if i == 0:
        table[i].append("HRID\n")
    else:
        table[i].append(f"{table[i][1]}-{table[i][2]}-{table[i][3]}-{table[i][6]}\n")

for i in range(0, 61):
    table[i] = ",".join(table[i])

writeFile(table)

        
            

    
    
