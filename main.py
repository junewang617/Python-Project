#Import modules
import os
import csv

#CSV path to collect data
csvpath = os.path.join('..', 'PyPoll','Resources','election_data.csv')

#Initiate total vote count and cadidate list
total_votes = 0
candidate = []

#Read through each row after header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #Loop through each row of data to increment vote count and push to candidate array
    for row in csvreader:
        total_votes += 1
        candidate.append(row[2])

#Create dictionary for the number of votes per candidate
candidate_count = dict((i,candidate.count(i)) for i in set(candidate))
#Get winner with max value within dictionary 
winner = max(candidate_count, key=candidate_count.get)

#Print results in terminal
print("Election Results")
print("-------------------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------------------")
#Loop through dictionary and disply each dictionary key with total and percentage of votes
for key in candidate_count:
    print(f'{key}: {(candidate_count[key]/total_votes):.3%} ({candidate_count[key]})')
print("-------------------------------------------")
print(f'Winner: {winner}')
print("-------------------------------------------")


# Create and print analysis output and export to textfile
output_path = os.path.join('..', 'PyPoll', 'Analysis', 'poll_output.txt')
f = open(output_path, "w")

print("Election Results", file=f)
print("-------------------------------------------", file=f)
print(f'Total Votes: {total_votes}', file=f)
print("-------------------------------------------", file=f)
for key in candidate_count: 
    print(f'{key}: {(candidate_count[key]/total_votes):.3%} ({candidate_count[key]})', file=f)
print("-------------------------------------------", file=f)
print(f'Winner: {winner}', file=f)
print("-------------------------------------------", file=f)

f.close()



    
   
