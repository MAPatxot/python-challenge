#PyPoll - Homework 3

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# 1- The total number of votes cast
# 2- A complete list of candidates who received votes
# 3- The percentage of votes each candidate won
# 4- The total number of votes each candidate won
# 5- The winner of the election based on popular vote.


# import os and csv
import os
import csv

# Columns from CSV are labeled as Voters ID, County, and Candidate -- [] 
voter_id = []
county = []
candidate = []
# unique = [] # for find the list of candidates?
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_reader = next(csvreader, None)
    header = next(csvreader, None)

#1 - The total number of votes cast ; used the same format as PyBank
    total_votes += 1
    
    for header in csvreader:
        total_votes += 1
    #print(f"Total Votes: {total_votes}")

#2 - A complete list of candidates who received votes -- ??? -- StackOverflow - 
# https://stackoverflow.com/questions/24441606/how-to-create-a-list-in-python-with-the-unique-values-of-a-csv-file
    #     if header[2] not in candidate:
    #         candidate.append(header[2])
    # print(candidate)


#4 - The total number of votes each candidate won; create a variable for the output for votes
# for Khan - khan_votes, correy_votes, li_variables, otooley_votes - need to find a way to choose out
# these four names from the list -- names are in header[2]
        if (header[2]== "Khan"):
            khan_votes += 1
#print(f"Khan Total Votes: {khan_votes}")
        elif (header[2] == "Correy"):
            correy_votes += 1
#print(f"Correy Total Votes: {correy_votes}")
        elif (header[2] == "Li"):
            li_votes += 1
#print(f"Li Total Votes: {li_votes}")           
        else:
            otooley_votes += 1
#print(f"O'Tooley Total Votes: {otooley_votes}")

#3 - The percentage of votes each candidate won
    khan_percent = ((khan_votes/total_votes)*100)
#print(f"Khan Percent: %{khan_percent:.2f}")
    correy_percent = ((correy_votes/total_votes)*100)
#print(f"Correy Percent: %{correy_percent:.2f}")
    li_percent = ((li_votes/total_votes)*100)
#print(f"Li Percent: %{li_percent:.2f}")
    otooley_percent = ((otooley_votes/total_votes)*100)
#print(f"O'Tooley Percent: %{otooley_percent:.2f}")

#5 - The winner of the election based on popular vote.
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

#print(f"Winner: {winner_name}")

# 6 - Print Statements
print(f"")
print(f"Election Results")
print(f"---------------------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"---------------------------------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------------------------------")
print(f"")