"""
Author: Andrea Kristine S. Pongco
Date of Development: December 4, 2023
Course: CMSC 191/BIO 191 (Laboratory Exam)
"""

import pandas as pd

df = pd.read_csv('../Exam_Table.csv') #read csv file
df = df.T #transpose the data

df.to_csv('b7_output1.csv', index=False)

        
            

    
    
