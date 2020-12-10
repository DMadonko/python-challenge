import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv, "r") as election_file:
    election_csv_reader = csv.reader(election_file, delimiter = ",")
    header = next(election_csv_reader)

totalvotes = 0
candidates = {}
percentage_votes = 0
num_votes = 0
popvote = 0
winner = ""

# The total number of votes cast
for row in election_csv_reader:
    totalvotes += 1
    
    if row[2] in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1
    else:
            candidates[row[2]] = 1

# The percentage of votes each candidate won
percentage_votes = (candidates[row[2]])/(totalvotes) * 100

# The total number of votes each candidate won
for row[2] in candidates:
        num_votes += candidates[row[2]]

# The winner of the election based on popular vote.
if candidates[row[2]]> popvote:
            winner = row[2]
            popvote = candidates[row[2]]

print("Election Results")
print("------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
print(f"{row[2]}: {int(percentage_votes)}% {num_votes}")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")