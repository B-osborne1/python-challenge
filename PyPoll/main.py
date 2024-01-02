import csv
import os

# open the file in read mode
filename = open('Resources/election_data.csv', 'r')

# Using dictreader to avoid top row
pypoll = csv.DictReader(filename)

# grab column that will be untouched for length (unnecessary, but safe)
county = []

#Start dictionary to define both the candidates and their total votes
candidate_counts = {}
percentage = 0

for col in pypoll:
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


#Find who had the most votes
        #Use key to avoid last candidate overriding candidate with most votes
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

    #State the candidate with the highest votes
print("-------------------")
print("Winner=", elected)

# Set variable for output file
output_file = os.path.join("Analysis/pypoll_analysis.csv")


#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Candidate", "Number of votes", "Total votes", "Winner"])

    # Write rows
    for candidate, count in candidate_counts.items():
        # Write each candidate's information
        writer.writerow([candidate, count, len(county), elected])
