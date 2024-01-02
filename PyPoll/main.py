import csv
import pandas as pd

# open the file in read mode
filename = open('Resources/election_data.csv', 'r')

# creating dictreader object
file = csv.DictReader(filename)

# grab column that will be untouched for length
county = []

#Start dictionary to define both the candidates and their total votes
candidate_counts = {}


for col in file:
        #Finding total number of votes
    county.append(col["County"])

        #Recognising candidates in column
    candidate = col["Candidate"]

            # Either add the name or add the count
    #Adding to the count if name is already present
    if candidate in candidate_counts:
        candidate_counts[candidate] += 1
    # If name is not present, start count at 1 and enter name into dictionary
    else:
        candidate_counts[candidate] = 1

elected = max(candidate_counts, key=candidate_counts.get)


#Printing -- overall results
    #Title
print("Election Results")
print("-------------------")

    #Total number of votes
print("Number of Votes: ", len(county))
print("-------------------")

    #Candidates and number of votes each
for candidate, count in candidate_counts.items():
    print(f"{candidate}: {count} votes")

print("-------------------")
print(elected)