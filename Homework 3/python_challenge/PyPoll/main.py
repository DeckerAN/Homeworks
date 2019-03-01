# *** PyPoll ***

# Importing the csv module to read the file
import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Variables that need defining
Vote_Counter = 0

# Within the csv file...
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        # Counting rows for Total Votes
        Vote_Counter += 1


Poll_Results = f"""    Election Results
    ----------------------------
    Total Votes: {Vote_Counter}
    ----------------------------
    :  
    : 
    ----------------------------
    Winner:
    """

print(Poll_Results)

#output_file = open("PyPoll_output.txt", "w")

#output_file.write(Poll_Results)