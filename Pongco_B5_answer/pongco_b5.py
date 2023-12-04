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
    with open("./b5_output1.csv", "w", encoding="utf-8-sig") as file:
        file.writelines(filtered_table)

table = readCSVFile()
pomacentrus_adelus = []

for i in range(0, 61):
    table[i] = table[i].split(",")
    table[i] = table[i][-3:-1]

for i in range(0, 61):
    if table[i][0] == "Pomacentrus adelus":
        pomacentrus_adelus.append(table[i])

summation = 0
for i in range(0, len(pomacentrus_adelus)):
    summation += int(pomacentrus_adelus[i][1])
average = summation/len(pomacentrus_adelus)

write_in_file = [f"{table[0][0]},Average Count\n", f"Pomacentrus adelus,{average}"]

writeFile(write_in_file)
        
            

    
    
