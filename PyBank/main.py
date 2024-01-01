import os
import csv

    #Path to main file
pybank_csv = os.path.join("Resources", "budget_data.csv")


row_count = 0
column_count = 1
column_1 = 1
column_sum = 0

    #Title
print("Financial Analysis")
print("--------------------------------")
    
    #Open main file
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Ignore the initial title row
    next(csvreader, None)

    #Part 1: Total number of months - Sum of rows used excluding title
    for row in csvreader:
        if len(row) > column_count:
            row_count += 1


    print(f'Total number of months = {row_count}')
#Look back at this -- current failure
                    #Part 2: Net gain/loss - Sum of values in rows excluding title
                    for row in csvreader:
                        if len(row) > column_sum and row[column_1]:
                            column_sum += float(row[column_1])

                    print(f'Total profit over period = {column_sum}')
    #Part 3: Average change per month



    #Part 4: Greatest increase/decrease (name and quantity)

