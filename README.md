# python-challenge

This repository utilises python and the csv system to analyse excel spreadsheets. It is split into two independent sections: PyBank and Pypoll. Both these folders contain the python script, a resources folder containing base analysis material, and an analysis folder from the python script

1) PyBank

This folder contains an analysis on the changes over time (monthly) that a company logged. The focus is on finding the length in months, followed by total/average changes and min/max months.

Notes:  Use of dictreader at line 7 to avoid header rows was from a source that was lost before noting
Analysis file has had its headers adjusted which will be overriden when code used
 
2) PyPoll

This folder analyses the results of a poll/election and the results of such. It indicates all candidates with votes, the number of votes they received and who the winner was

Notes:
Issue 1- Was unsuccessful at extracting percentages from each candidates votes and is missing from the code and analysis

Issue 2- When transferring script into analysis, the winner and total votes are iterated for all rows

Line 26, 27, 30 and 35 were heavily assisted with the use of AI
