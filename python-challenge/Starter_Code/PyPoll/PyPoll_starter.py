# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
Charles_count = 0
Diana_count = 0
Raymon_count = 0
vote_count_ls = []
print("The candidates are Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane.")


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        vote_count_ls.append(row[1])
        vote_count = int(len(vote_count_ls))

        # Get the candidate's name from the row
        if row[2] == "Charles Casper Stockham":
            Charles_count = Charles_count + 1
            Charles_percentage = ((Charles_count / vote_count)* 100)
        if row[2] == "Diana DeGette":
            Diana_count = Diana_count + 1
            Diana_percentage = ((Diana_count / vote_count)* 100)
        if row[2] == "Raymon Anthony Doane":
            Raymon_count = Raymon_count + 1
            Raymon_percentage = ((Raymon_count / vote_count)* 100)

    # Print the total vote count (to terminal)
    print(f'The total vote count was {vote_count}!')

    # Loop through the candidates to determine vote percentages and identify the winner
    if Charles_percentage > Raymon_percentage and Diana_percentage:
        winner = "Charles Casper Stockham"
    if Diana_percentage > Raymon_percentage and Charles_percentage:
        winner = "Diana DeGette"
    if Raymon_percentage > Diana_percentage and Charles_percentage:
        winner = "Raymon Anthony Doane"

    print(f'Total votes:  {vote_count}.')
    print(f'Total votes for Charles Casper Stockham: {Charles_count} ({Charles_percentage}%).')
    print(f'Total votes for Diana DeGette: {Diana_count} ({Diana_percentage}%).')
    print(f'Total votes for Raymon Anthony Doane: {Raymon_count} ({Raymon_percentage}%).')

    print(f'Winner: {winner}')


with open(file_to_output, "w", newline ='\n') as txt_file:
    txt_file.write(f'Total votes:  {vote_count}.\n')
    txt_file.write(f'Total votes for Charles Casper Stockham: {Charles_count} ({Charles_percentage}%).\n')
    txt_file.write(f'Total votes for Diana DeGette: {Diana_count} ({Diana_percentage}%).\n')
    txt_file.write(f'Total votes for Raymon Anthony Doane: {Raymon_count} ({Raymon_percentage}%).\n')
    txt_file.write(f'Winner: {winner}\n')

