import os
import csv

# Specify the file to write to (Using os library so that the path is machine/OS agnostic)
output_path = os.path.join('analysis', 'election_analysis.txt')
csvpath = os.path.join('Resources', 'election_data.csv')

# Variables
candidates = []
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        candidate = row[2]
        total_votes += 1

        # Create list of all candidates
        if candidate not in candidates:
            candidates.append(candidate)

        # Tally votes
        if candidate == 'Charles Casper Stockham':
            charles_votes += 1
        if candidate == 'Diana DeGette':
            diana_votes += 1
        if candidate == 'Raymon Anthony Doane':
            raymon_votes += 1

# Find the candidate with the most votes and declare the winner
all_votes = [charles_votes, diana_votes, raymon_votes]
max_votes = max(all_votes)

if max_votes == charles_votes:
    winner = 'Charles Casper Stockham'
elif max_votes == diana_votes:
    winner = 'Diana DeGette'
elif max_votes == raymon_votes:
    winner = 'Raymon Anthony Doane'

# Create a new text file + print to terminal
with open(output_path, 'w') as file:
    file.write(f'Election Results \n')
    file.write(f'\n---------------------------- \n')
    file.write(f'\n Total Votes: {total_votes} \n')
    file.write(f'\n---------------------------- \n')
    file.write(f'\n Charles Casper Stockham:  {(charles_votes / total_votes) * 100:.3f}% ({charles_votes}) \n')
    file.write(f'\n Diana DeGette: {(diana_votes / total_votes) * 100:.3f}% ({diana_votes}) \n')
    file.write(f'\n Raymon Anthony Doane: {(raymon_votes / total_votes) * 100:.3f}% ({raymon_votes})  \n')
    file.write(f'\n---------------------------- \n')
    file.write(f'\n Winner: {winner}  \n')
    file.write(f'\n----------------------------')


print(f'Election Results \n')
print(f'\n---------------------------- \n')
print(f'\n Total Votes: {total_votes} \n')
print(f'\n---------------------------- \n')
print(f'\n Charles Casper Stockham:  {(charles_votes / total_votes) * 100:.3f}% ({charles_votes}) \n')
print(f'\n Diana DeGette:  {(diana_votes / total_votes) * 100:.3f}% ({diana_votes}) \n')
print(f'\n Raymon Anthony Doane:  {(raymon_votes / total_votes) * 100:.3f}% ({raymon_votes})  \n')
print(f'\n---------------------------- \n')
print(f'\n Winner: {winner}  \n')
print(f'\n----------------------------')