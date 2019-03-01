# *** PyPoll ***

# Importing the csv module to read the file
import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Variables that need defining
Vote_Counter = 0
Candidates = {}
Max_Votes = 0

# Within the csv file...
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Until I need the headers, this just destroys the header row for following script
    csv_header = next(csvreader)

    for row in csvreader:
        # Counting rows for Total Votes
        Vote_Counter += 1
        # Adding each unique candidate to create a complete dict of candidates as keys...
        if row[2] not in Candidates:
            Candidates[row[2]] = 0
        # ... and their votes as values
        else:
            Candidates[row[2]] += 1
    
    for kCand in Candidates:
        if Max_Votes < Candidates[kCand]:
            Max_Votes = Candidates[kCand]
            Winner = kCand
    

print(f"""
Election Results
----------------------------
Total Votes: {Vote_Counter}
----------------------------""")
# Below is printing each key (candidate), each value (votes) over total votes to get percentage of votes, and each value (votes)
for k, v in Candidates.items():
        print(k + ": " + str(round((v / Vote_Counter) * 100)) + "% (" + str(v) + ")")    
print(f"""----------------------------
Winner: {Winner}
    """)


#output_file = open("PyPoll_output.txt", "w")

#output_file.write(Poll_Results)