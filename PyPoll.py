# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = 'Resources1/election_results.csv'

# Assign a variable to save a file to a path.
file_to_save = os.path.join("C:/Users/andre/Documents/Analysis_Projects/Election_Analysis/analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    for row in file_reader:
        print(row)
